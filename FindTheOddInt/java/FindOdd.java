
import java.util.Map;
import java.util.HashMap;

public class FindOdd {
	public static int findIt(int[] a) {
		Map<Integer, Integer> dict = new HashMap<>();
		
		for(int num : a){
			if(dict.containsKey(num)) {
				dict.put(num, dict.get(num) + 1);
			} else {
				dict.put(num, 1);
			}
		}
	
		for(int key : dict.keySet()) {
			if(dict.get(key) % 2 != 0){
				return key;
			}
		}

		return 0;
  }
}
