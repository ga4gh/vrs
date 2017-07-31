// Demonstrates how to construct a VMC Digest from a sample serialization string

// snafu$ javac VMCDigestExample.java 
// snafu$ java VMCDigestExample 
// ser = <Location:<Identifier:VMC:GS_IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl>:<Interval:44908683:44908684>>
// vmc digest = 9Jht-lguk_jnBvG-wLJbjmBw5v_v7rQo

// Matches output from python:
// $ ipython
// In [1]: import hashlib, base64
// 
// In [2]: ser = "<Location:<Identifier:VMC:GS_IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl>:<Interval:44908683:44908684>>"
// 
// In [3]: base64.urlsafe_b64encode(hashlib.sha512(ser.encode("ASCII")).digest()[:24])
// Out[3]: b'9Jht-lguk_jnBvG-wLJbjmBw5v_v7rQo'


import static java.nio.charset.StandardCharsets.*;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;

class VMCDigestExample {  
    public static void main(String args[]){  
	Object o = null;
	String ser = serialize(o);
	byte[] serb = ser.getBytes(US_ASCII);
	String vmcdigest = base64us(sha512t24(serb));
	System.out.println("ser = " + ser);
	System.out.println("vmc digest = " + vmcdigest);
    }  

    public static String serialize(Object o) {
	// This is a mock function to return an example serialization.
	// In a real implementation that supports VMC, this function
	// would need to support serializing any VMC object, i.e.,
	// Identifier, Location, Allele, Haplotype, or Genotype.  The
	// formats for serialization are in the VMC Specification.
	// Also see the Python implementation here:
	// https://github.com/ga4gh/vmc/blob/dev/demo/vmcdemo/digest.py#L67
	return "<Location:<Identifier:VMC:GS_IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl>:<Interval:44908683:44908684>>";
    }

    private static byte[] sha512t24(byte[] bytes) {
	// return the 24-byte truncated SHA-512 for `bytes`
	// XXX add reference to statistics
	MessageDigest md = null;
	try {
	    md = MessageDigest.getInstance("SHA-512");
	} catch (NoSuchAlgorithmException e) {
	    e.printStackTrace();
	}

	byte[] digest = md.digest(bytes);
	byte[] digest24 = Arrays.copyOfRange(digest, 0, 24);
	return digest24;
    }

    private static String base64us(byte[] bytes) {
	// returns URL-Safe Base64 encoded String for bytes
	// https://tools.ietf.org/html/rfc3548#section-4
	// getUrlEncoder().encodeToString(bytes) is comparable to
	// Python's base64.urlsafe_b64encode(bytes)
	return Base64.getUrlEncoder().encodeToString(bytes);
    }


