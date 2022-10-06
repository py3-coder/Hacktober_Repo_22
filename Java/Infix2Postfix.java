import java.util.*;

public class Infix2Postfix {
    static String convertPostfix(String infix) {
        Stack<Character> st = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < infix.length(); i++) {
            // if spaces ignore
            if (infix.charAt(i) == ' ') {
                continue;
            }
            // if operand print
            if (isOperand(infix.charAt(i))) {
                sb.append(infix.charAt(i));
            } else if (infix.charAt(i) == '(') { // push if (
                st.push(infix.charAt(i));
            } else if (infix.charAt(i) == ')') { // pop until find ( if char is )
                while (st.peek() != '(') {
                    sb.append(st.pop()); // print the popped chars
                }
                st.pop(); // and finally pop (
            } else {
                if (st.isEmpty()) { // if empty then push
                    st.push(infix.charAt(i));
                } else {
                    // check for precedences
                    if (precedence(infix.charAt(i)) > precedence(st.peek())) {
                        st.push(infix.charAt(i));
                    } else {
                        while (!st.isEmpty() && precedence(infix.charAt(i)) <= precedence(st.peek())) {
                            sb.append(st.pop());
                        }
                        st.push(infix.charAt(i));
                    }
                }
            }
        }
        // pop all the remaining elements in stack and print it
        while (!st.isEmpty()) {
            sb.append(st.pop());
        }
        // return
        return sb.toString();
    }

    static boolean isOperand(char ch) {
        // if character is alphabet then it is an operand
        if (ch >= 'a' && ch <= 'z') {
            return true;
        } else if (ch >= 'A' && ch <= 'Z') {
            return true;
        }
        return false;
    }

    static int precedence(char ch) {

        // precedence order ( < + = - < / = *
        if (ch == '*' || ch == '/') {
            return 2;
        } else if (ch == '+' || ch == '-') {
            return 1;
        } else if (ch == '(') {
            return 0;
        }
        return 0;
    }

    public static void main(String[] args) {
        String infix = "A+B*C/(E-F)  ";
        String postfix = convertPostfix(infix);
        System.out.println(postfix);
    }
}
