public class Persist {
	public static int persistence(long n) {
		// your code
		String n_s = "" + n;
		int count = 0;

		while(true){
			int total = 1;
			int currentLen = n_s.length();
			
			for(int i = 0; i < currentLen; i++) {
				total *= (n_s.charAt(i) - '0');
			}

			n_s = "" + total;

			if(currentLen == 1) return count; else count += 1;
		}
	
	}
	
}
