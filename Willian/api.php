<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: GET, POST");

function removerAcentos($string) {
    return preg_replace(array("/(á|à|ã|â|ä)/","/(Á|À|Ã|Â|Ä)/","/(é|è|ê|ë)/","/(É|È|Ê|Ë)/","/(í|ì|î|ï)/","/(Í|Ì|Î|Ï)/","/(ó|ò|õ|ô|ö)/","/(Ó|Ò|Õ|Ô|Ö)/","/(ú|ù|û|ü)/","/(Ú|Ù|Û|Ü)/","/(ñ)/","/(Ñ)/","/(ç)/","/(Ç)/"),explode(" ","a A e E i I o O u U n N c C"),$string);
}

$acao = isset($_GET['acao']) ? $_GET['acao'] : null;

$inputJSON = file_get_contents('php://input');
$input = json_decode($inputJSON, true);

if (!$input) {
    if (!empty($_POST)) {
        $input = $_POST;
    } else {
        $input = $_GET;
    }
}

$response = [
    'status' => 'erro',
    'mensagem' => 'Ação não definida ou inválida.'
];

if ($acao) {
    switch ($acao) {
        
        case 'calcular_imc':
            $pesoRaw = isset($input['peso']) ? str_replace(',', '.', $input['peso']) : 0;
            $alturaRaw = isset($input['altura']) ? str_replace(',', '.', $input['altura']) : 0;

            $peso = floatval($pesoRaw);
            $altura = floatval($alturaRaw);

            if ($peso > 0 && $altura > 0) {
                $imc = $peso / ($altura * $altura);
                $classificacao = '';

                if ($imc < 18.5) {
                    $classificacao = 'Abaixo do peso';
                } elseif ($imc < 25) {
                    $classificacao = 'Peso normal';
                } elseif ($imc < 30) {
                    $classificacao = 'Sobrepeso';
                } elseif ($imc < 35) {
                    $classificacao = 'Obesidade grau I';
                } elseif ($imc < 40) {
                    $classificacao = 'Obesidade grau II';
                } else {
                    $classificacao = 'Obesidade grau III';
                }
                
                $response = [
                    'status' => 'sucesso',
                    'dados' => [
                        'imc' => round($imc, 2),
                        'classificacao' => $classificacao
                    ]
                ];
            } else {
                $response['mensagem'] = 'Peso e altura devem ser maiores que zero.';
            }
            break;

        case 'verificar_palindromo':
            $texto = isset($input['texto']) ? $input['texto'] : '';
            
            $semAcentos = removerAcentos($texto);
            $limpo = strtolower(preg_replace('/[^A-Za-z0-9]/', '', $semAcentos));
            
            if (!empty($limpo)) {
                $invertido = strrev($limpo);
                $ehPalindromo = ($limpo === $invertido);
                
                $response = [
                    'status' => 'sucesso',
                    'dados' => [
                        'texto_original' => $texto,
                        'texto_tratado' => $limpo,
                        'eh_palindromo' => $ehPalindromo
                    ]
                ];
            } else {
                $response['mensagem'] = 'Envie um texto válido contendo letras ou números.';
            }
            break;

        case 'gerar_tabuada':
            if (!isset($input['numero']) || $input['numero'] === '') {
                $response['mensagem'] = 'O parâmetro "numero" é obrigatório.';
                break;
            }

            $numeroRaw = str_replace(',', '.', $input['numero']);

            if (!is_numeric($numeroRaw)) {
                $response['mensagem'] = 'O valor informado não é um número válido.';
            } else {
                $numero = floatval($numeroRaw);
                $resultados = [];

                for ($i = 1; $i <= 10; $i++) {
                    $res = $numero * $i;
                    $resFormatado = (float)$res; 
                    $resultados[] = "$numero x $i = " . $resFormatado;
                }

                $response = [
                    'status' => 'sucesso',
                    'dados' => $resultados
                ];
            }
            break;

        case 'info_sistema':
            $response = [
                'status' => 'sucesso',
                'dados' => [
                    'data_hora' => date('Y-m-d H:i:s'),
                    'versao_php' => phpversion(),
                    'servidor' => $_SERVER['SERVER_SOFTWARE'] ?? 'Desconhecido',
                    'metodo_requisicao' => $_SERVER['REQUEST_METHOD']
                ]
            ];
            break;
            
        default:
            $response['mensagem'] = "Método '$acao' não encontrado.";
            break;
    }
}

echo json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
