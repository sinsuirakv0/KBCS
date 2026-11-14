# 00bf3cfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bf3cfc",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_RKS4_",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30b9515588040678ec18cb9f745b36ebddb7fd61982468964d6d4fc301e723e3",
  "source_text_sha256": "30b9515588040678ec18cb9f745b36ebddb7fd61982468964d6d4fc301e723e3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006d7aec](../006d7/006d7aec.md)

## 疑似コード / UTF-8 501 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC1ERKS5_RKS4_
               (undefined8 *param_1,byte *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_2 & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)param_2;
    param_1[2] = *(undefined8 *)(param_2 + 0x10);
    param_1[1] = uVar2;
    *param_1 = uVar1;
    return;
  }
  FUN_006d7aec(param_1,*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
  return;
}

~~~
