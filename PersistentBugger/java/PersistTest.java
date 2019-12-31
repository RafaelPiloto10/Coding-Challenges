public class PersistTest {
   
	static int num = 0;

	public static void assertEquals(int exp, int obs){
		num += 1;
		boolean passed = exp == obs;
		System.out.println("Test #" + num + (passed ? " PASSED" : " FAILED"));

		if(!passed) {
			System.out.println("Expected: " + exp);
			System.out.println("Got: " + obs);
		}
	}

	public static void BasicTests() {
		System.out.println("****** Basic Tests ******");
		assertEquals(3, Persist.persistence(39));
		assertEquals(0, Persist.persistence(4));
		assertEquals(2, Persist.persistence(25));
		assertEquals(4, Persist.persistence(999));
	}

	public static void main(String[] args) {
		BasicTests();
	}
	
}

