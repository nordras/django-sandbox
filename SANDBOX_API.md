# 📊 **Swagger API do Sandbox - Guia Completo**

## 🎯 **URLs da API**

### **Interface Web**
- **Sandbox Interface**: `http://localhost:8000/sandbox/`
- **Execução Individual**: `http://localhost:8000/sandbox/run/{id}/`

### **API REST com Swagger**
- **API Sandbox**: `http://localhost:8000/sandbox/api/`
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`

## 🚀 **Endpoints Disponíveis**

### **1. Listar Algoritmos**
```
GET /sandbox/api/
```
Retorna lista completa de algoritmos com ID, nome, descrição e função.

### **2. Executar Algoritmo Individual**
```
GET /sandbox/api/{id}/
```
Executa algoritmo específico com dados padrão e métricas de performance.

### **3. Executar Todos os Algoritmos**
```
POST /sandbox/api/run_all/
```
Executa todos os 9 algoritmos e retorna resultados com métricas agregadas.

### **4. Two Sum Customizado**
```
POST /sandbox/api/two_sum_custom/
```
Executa Two Sum com entrada personalizada.

**Exemplo de Body:**
```json
{
  "nums": [3, 2, 4],
  "target": 6
}
```

## 📋 **Exemplos de Uso**

### **PowerShell**
```powershell
# Listar algoritmos
Invoke-RestMethod -Uri "http://localhost:8000/sandbox/api/" -Method GET

# Executar algoritmo específico (ID 5 = Valid Palindrome)
Invoke-RestMethod -Uri "http://localhost:8000/sandbox/api/5/" -Method GET

# Executar todos
Invoke-RestMethod -Uri "http://localhost:8000/sandbox/api/run_all/" -Method POST

# Two Sum customizado
$body = @{ nums = @(1, 2, 3, 4); target = 7 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/sandbox/api/two_sum_custom/" -Method POST -Body $body -ContentType "application/json"
```

### **cURL**
```bash
# Listar algoritmos
curl -X GET http://localhost:8000/sandbox/api/

# Executar algoritmo específico
curl -X GET http://localhost:8000/sandbox/api/5/

# Executar todos
curl -X POST http://localhost:8000/sandbox/api/run_all/

# Two Sum customizado
curl -X POST http://localhost:8000/sandbox/api/two_sum_custom/ \
  -H "Content-Type: application/json" \
  -d '{"nums": [1, 2, 3, 4], "target": 7}'
```

## 🔧 **Recursos do Swagger**

### **Documentação Automática**
- **Schemas**: Todos os serializers documentados
- **Exemplos**: Requests e responses de exemplo
- **Validação**: Validação automática de entrada
- **Métricas**: Tempo de execução para cada algoritmo

### **Tags Organizadas**
- **Sandbox**: Endpoints básicos do sandbox
- **Algoritmos Customizados**: Execução com entrada personalizada
- **API Principal**: Endpoints da API randori_doctor

### **Features Avançadas**
- **Deep Linking**: URLs diretas para endpoints
- **Try it Out**: Teste direto na interface
- **Schemas Detalhados**: Documentação completa dos dados
- **Persistent Auth**: Autenticação persistente (se habilitada)

## 🎯 **Próximos Passos**

1. **Adicionar mais algoritmos customizados**
2. **Implementar autenticação JWT**
3. **Adicionar rate limiting**
4. **Criar dashboard de métricas**
5. **Exportar resultados em diferentes formatos**

---

*Use o Swagger UI em `/api/docs/` para explorar interativamente todos os endpoints!*
