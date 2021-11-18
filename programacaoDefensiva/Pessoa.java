public final class Pessoa {

    private final String nome;
    private final String sobrenome;
    private final String rg;
    private final String cpf;

    private static class Builder {

        // parametros_obrigatorios
        private final String nome;
        private final String sobrenome;

        // parametros_opcionais
        private String rg = "";
        private String cpf = "";

        public Builder(String nome, String sobrenome) {
            this.nome = nome;
            this.sobrenome = sobrenome;

        }

        public Builder rg(String valor) {
            rg = valor;
            return this;
        }

        public Builder cpf(String valor) {
            cpf = valor;
            return this;
        }

        public Pessoa build() {
            return new Pessoa(this);
        }
    }

    private Pessoa(Builder builder) {
        nome = builder.nome;
        sobrenome = builder.sobrenome;
        rg = builder.rg;
        cpf = builder.cpf;
    }

    public static void main(String[] args) {

        // Pessoa p = new Pessoa("nomjuca");
        Pessoa p1 = new Pessoa.Builder("nomjuca", "pira").build();

        Pessoa p2 = new Pessoa.Builder("noel", "da viola").cpf("092.444.555.62").build();

        System.out.println(p1);
        System.out.println(p2);
    }

}