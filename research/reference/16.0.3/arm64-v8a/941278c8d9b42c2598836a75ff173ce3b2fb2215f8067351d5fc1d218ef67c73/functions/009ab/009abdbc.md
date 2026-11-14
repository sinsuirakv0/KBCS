# 009abdbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009abdbc",
  "name": "FUN_009abdbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98a73b8c94db259919c9b08deaea28b4af061aa994b4f40e71bf7f20268b09d7",
  "source_text_sha256": "98a73b8c94db259919c9b08deaea28b4af061aa994b4f40e71bf7f20268b09d7"
}
~~~

## 呼び出し元

- [00764918](../00764/00764918.md)
- [009b0ea8](../009b0/009b0ea8.md)
- [009b6d74](../009b6/009b6d74.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009abdbc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x4c);
  uVar1 = *(undefined4 *)(param_2 + 0x5c);
  param_1[1] = *(undefined8 *)(param_2 + 0x54);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~
