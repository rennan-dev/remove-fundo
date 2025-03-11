## Remoção de Fundo de Imagens em Python

Este projeto permite remover o fundo de imagens automaticamente usando a biblioteca `rembg`.

### 1. Pré-requisitos

Antes de executar o script, instale as dependências necessárias:

```sh
pip install rembg pillow
```

### 2. Como Usar

Execute o script passando o caminho da imagem de entrada e o nome do arquivo de saída:

```sh
python main.py imagem_entrada.jpg imagem_saida.png
```

### 3. Explicação do Código

- O script carrega a imagem usando `PIL` (Pillow);
- Utiliza a biblioteca `rembg` para remover o fundo;
- Salva a nova imagem em formato PNG (para manter a transparência).

### 4. Exemplo de Uso

Se você tem uma imagem chamada `foto.jpg` e deseja salvar o resultado como `foto_sem_fundo.png`, execute:

```sh
python remove_bg.py foto.jpg foto_sem_fundo.png
```

A saída será uma imagem sem fundo salva no diretório especificado.

### 5. Observações

- O modelo de remoção de fundo é treinado para reconhecer objetos e pessoas;
- Os melhores resultados ocorrem com imagens de alta qualidade e fundo bem definido;
- Para otimizar a performance, recomenda-se usar imagens de tamanho adequado.

