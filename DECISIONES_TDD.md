# Diario TDD

## Ciclo 1

### Red
- Prueba añadida: test_one_feature_is_tiny (prueba inicial), test_two_feature_is_tiny, test_three_feature_is_not_tiny
- Técnica de diseño de pruebas empleada: buscar casos límite
- Motivo de elegir este caso: caso más básico
- Fallo observado: la función daba NotImplementedError porque no estaba implementada (duh), cuando debía devolver "tiny"

### Green
- Código mínimo escrito: el caso "tiny" (1 <= feature_count <= 5)
- Resultado de las pruebas: pasan todas

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: (n/p)

---

Copiad este bloque para cada ciclo.
