# 00abe7fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00abe7fc",
  "name": "FUN_00abe7fc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2",
  "source_text_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2"
}
~~~

## 呼び出し元

- [006ee798](../006ee/006ee798.md)
- [006f252c](../006f2/006f252c.md)
- [00a52034](../00a52/00a52034.md)

## 呼び出し先

- [00abd080](../00abd/00abd080.md)

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00abe7fc(long param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  
  iVar2 = FUN_00abd080();
                    /* catch() { ... } // from try @ 00abe684 with catch @ 00abe828 */
  iVar1 = iVar2 + param_3;
  if (1999999999 < iVar2 + param_3) {
    iVar1 = 2000000000;
  }
  if (param_2 == 4) {
    *(int *)(param_1 + 0x68) = iVar1;
  }
  else if (param_2 == 1) {
    *(int *)(param_1 + 100) = iVar1;
  }
  else if (param_2 == 0) {
    *(int *)(param_1 + 0x60) = iVar1;
  }
  return;
}

~~~
