package com.example.lab1a;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void factorization(View view) {
        try{
            EditText editText = findViewById(R.id.input);
            TextView textView = findViewById(R.id.output);
            TextView textIterations = findViewById(R.id.iterations);
            int num = Integer.parseInt(editText.getText().toString());
            int a = (int) Math.ceil(Math.sqrt(num));
            int countIter = 0;
            if ((num & 1) == 0) {
                textView.setText("Число є парним:\n" + num + " = " + num / 2 + " * " + 2);
            } else {
                while (!isSquare(a * a - num)) {
                    a+=1;
                    countIter+=1;
                }
                int b = (int) Math.sqrt(a * a - num);
                textView.setText("Результат факторизації:\n"  + num + " = " + (a + b) + " * " + (a - b));
                textIterations.setText("Кількість проведених ітерацій на пошук відповіді:\n"+ countIter);

            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public boolean isSquare(int n) {
        int sqr = (int) Math.sqrt(n);
        return sqr * sqr == n;
    }
}
