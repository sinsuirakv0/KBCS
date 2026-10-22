# 00aeacc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeacc8.md)

## 関数情報

~~~json
{
  "address": "00aeacc8",
  "name": "firebase::util::hash_map::RegisterNatives",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f374882ec32d3f7b181322cca8b4e8da1dec503fd995c0caf511d46c0911d612",
  "source_text_sha256": "f374882ec32d3f7b181322cca8b4e8da1dec503fd995c0caf511d46c0911d612"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 823 bytes

~~~c

/* firebase::util::hash_map::RegisterNatives(_JNIEnv*, JNINativeMethod const*, unsigned long) */

bool firebase::util::hash_map::RegisterNatives
               (_JNIEnv *param_1,JNINativeMethod *param_2,ulong param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0758 == '\0') {
                    /* catch() { ... } // from try @ 00aeab8c with catch @ 00aeacf8 */
    iVar3 = (**(code **)(*(long *)param_1 + 0x6b8))(param_1,DAT_010a0750,param_2,param_3);
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    DAT_010a0758 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0758;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
