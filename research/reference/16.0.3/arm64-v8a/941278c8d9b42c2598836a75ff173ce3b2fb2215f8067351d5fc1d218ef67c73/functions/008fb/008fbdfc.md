# 008fbdfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "008fbdfc",
  "name": "FUN_008fbdfc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3a804d3c10d39e0afa82079930694311a2468e2fdf7d77f459ab56c04558ece",
  "source_text_sha256": "f3a804d3c10d39e0afa82079930694311a2468e2fdf7d77f459ab56c04558ece"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008524fc](../00852/008524fc.md)
- [008ba17c](../008ba/008ba17c.md)

## 疑似コード / UTF-8 591 bytes

~~~c

void FUN_008fbdfc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar3 = *param_2;
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008fbd9c with catch @ 008fbe38 */
                    /* catch() { ... } // from try @ 008fbdc0 with catch @ 008fbe48 */
    *(uint *)(lVar2 + 0x4a844) = *(uint *)(lVar2 + 0x4a844) | 8;
    FUN_008ba17c(uVar3);
    return;
  }
  return;
}

~~~
