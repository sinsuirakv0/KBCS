# 00af3bac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af3bac.md)

## 関数情報

~~~json
{
  "address": "00af3bac",
  "name": "firebase::util::JObjectClassName",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5971cb10e1ecb643615ae852844e2ba6b51901d222e5b6606c7b060323bc56ac",
  "source_text_sha256": "5971cb10e1ecb643615ae852844e2ba6b51901d222e5b6606c7b060323bc56ac"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bddfa0](../00bdd/00bddfa0.md)

## 疑似コード 1/1 / UTF-8 845 bytes

~~~c

/* firebase::util::JObjectClassName(_JNIEnv*, _jobject*) */

void firebase::util::JObjectClassName(_JNIEnv *param_1,_jobject *param_2)

{
  char cVar1;
  undefined8 uVar2;
  _JNIEnv *p_Var3;
  _jobject *p_Var4;
  
  uVar2 = (**(code **)(*(long *)param_1 + 0xf8))();
  p_Var4 = DAT_010a05b0;
  p_Var3 = (_JNIEnv *)FUN_0047495c(param_1,uVar2);
  cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*(long *)param_1 + 0x80))(param_1);
    (**(code **)(*(long *)param_1 + 0x88))(param_1);
  }
  JStringToString((util *)param_1,p_Var3,p_Var4);
                    /* WARNING: Could not recover jumptable at 0x00af3c4c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*(long *)param_1 + 0xb8))(param_1,p_Var3);
  return;
}

~~~
