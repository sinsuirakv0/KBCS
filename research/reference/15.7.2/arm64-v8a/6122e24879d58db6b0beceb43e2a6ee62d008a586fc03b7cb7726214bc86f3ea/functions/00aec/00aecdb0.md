# 00aecdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecdb0.md)

## 関数情報

~~~json
{
  "address": "00aecdb0",
  "name": "firebase::util::set::RegisterNatives",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18759e36f79a473b622447c537c33491f1db7fae31bb6af7c62408d9bedb7035",
  "source_text_sha256": "18759e36f79a473b622447c537c33491f1db7fae31bb6af7c62408d9bedb7035"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 708 bytes

~~~c

/* firebase::util::set::RegisterNatives(_JNIEnv*, JNINativeMethod const*, unsigned long) */

bool firebase::util::set::RegisterNatives(_JNIEnv *param_1,JNINativeMethod *param_2,ulong param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a08d0 == '\0') {
    iVar3 = (**(code **)(*(long *)param_1 + 0x6b8))(param_1,DAT_010a08c8,param_2,param_3);
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    DAT_010a08d0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a08d0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
