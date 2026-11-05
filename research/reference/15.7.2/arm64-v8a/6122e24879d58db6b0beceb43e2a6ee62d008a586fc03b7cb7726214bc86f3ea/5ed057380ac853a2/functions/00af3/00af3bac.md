# 00af3bac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af3bac.md)

## 関数情報

~~~json
{
  "address": "00af3bac",
  "name": "_ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "087819567e945be810abefedcbcc6b15dd026294c2200781bf45aa233933984a",
  "source_text_sha256": "087819567e945be810abefedcbcc6b15dd026294c2200781bf45aa233933984a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bddfa0](../00bdd/00bddfa0.md)

## 疑似コード 1/1 / UTF-8 706 bytes

~~~c

void _ZN8firebase4util16JObjectClassNameEP7_JNIEnvP8_jobject(undefined8 param_1,long *param_2)

{
  char cVar1;
  undefined8 uVar2;
  
  uVar2 = (**(code **)(*param_2 + 0xf8))();
  uVar2 = FUN_0047495c(param_2,uVar2,DAT_010a05b0);
  cVar1 = (**(code **)(*param_2 + 0x720))(param_2);
  if (cVar1 != '\0') {
    (**(code **)(*param_2 + 0x80))(param_2);
    (**(code **)(*param_2 + 0x88))(param_2);
  }
  _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(param_1,param_2,uVar2);
                    /* WARNING: Could not recover jumptable at 0x00af3c4c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_2 + 0xb8))(param_2,uVar2);
  return;
}

~~~
