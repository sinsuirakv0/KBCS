# 00afca6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afca6c",
  "name": "FUN_00afca6c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ceb5c62fe7f298f1864c3a946b6bf42fb2f6f765d207e4f3178162bef539b2ff",
  "source_text_sha256": "ceb5c62fe7f298f1864c3a946b6bf42fb2f6f765d207e4f3178162bef539b2ff"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [00700f00](../00700/00700f00.md)
- [007082e8](../00708/007082e8.md)
- [00715908](../00715/00715908.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afca6c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849bc);
}

~~~
