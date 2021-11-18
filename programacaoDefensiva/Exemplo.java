import java.util.Optional;
import java.util.Random;

public class Exemplo {

    public static String getString() {
        return "OK";
    }

    public static Optional<String> getString2() {

        String retorno;

        if (new Random().nextInt(2) == 0) {

            retorno = null;

        } else {
            retorno = "OK";
        }

        return Optional.ofNullable(retorno);
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            Optional<String> op = getString2();
            if (op.isPresent()) {
                System.out.println(op.orElse("NULL"));
            }
        }
    }
}