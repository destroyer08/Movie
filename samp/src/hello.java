import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;


public class hello {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out.println("Hello World");
		Random randomGenerator = new Random();
		FileWriter fw = new FileWriter("out2.csv");
		int n = 50000, m = 10;
		for(int i=0;i<n;i++)
		{
			String temp = "";
			for(int j=0;j<m;j++)
			{
				int randomInt = randomGenerator.nextInt(8);
				temp = temp +"," +randomInt;
			}
			fw.write(temp+"\n");
		}
		fw.close();
	}

}
