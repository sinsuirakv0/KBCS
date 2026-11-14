# 00af4efc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af4efc",
  "name": "FUN_00af4efc",
  "size": 428,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "469d62adaf95a87a31593a3cc4f4f0a1da9ad7c7b7a7bca5609c8474ec3ee5c3",
  "source_text_sha256": "469d62adaf95a87a31593a3cc4f4f0a1da9ad7c7b7a7bca5609c8474ec3ee5c3"
}
~~~

## 呼び出し元

- [005f3680](../005f3/005f3680.md)
- [005f3e60](../005f3/005f3e60.md)
- [005f7d30](../005f7/005f7d30.md)
- [005f8c10](../005f8/005f8c10.md)
- [005f9aa0](../005f9/005f9aa0.md)
- [00707d34](../00707/00707d34.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 1272 bytes

~~~c

bool FUN_00af4efc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  if (((((*(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0) &&
        (lVar1 = FUN_008524fc(),
        *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 1)) &&
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 2)) &&
      ((lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xb &&
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xd)))) &&
     (lVar1 = FUN_008524fc(),
     *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0x10)) {
    if ((param_3 == -1) ||
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * -0xc804 + (long)param_3 * 0x3ec + 0x913e4) == 0)) {
      return false;
    }
    lVar1 = FUN_008524fc();
    if (*(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xe) {
      lVar1 = FUN_008524fc();
      return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) == 0xf;
    }
  }
  return true;
}

~~~
