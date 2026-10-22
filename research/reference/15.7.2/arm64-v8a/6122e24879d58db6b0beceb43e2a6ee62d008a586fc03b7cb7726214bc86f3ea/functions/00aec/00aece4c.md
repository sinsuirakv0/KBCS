# 00aece4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aece4c.md)

## 関数情報

~~~json
{
  "address": "00aece4c",
  "name": "firebase::util::set::ReleaseClass",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4ace42bb54a60bb0e50ba2d974a603efd8dc1ea197eafb109a809354d94caea",
  "source_text_sha256": "f4ace42bb54a60bb0e50ba2d974a603efd8dc1ea197eafb109a809354d94caea"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 609 bytes

~~~c

/* firebase::util::set::ReleaseClass(_JNIEnv*) */

void firebase::util::set::ReleaseClass(_JNIEnv *param_1)

{
  char cVar1;
  
  if (DAT_010a08c8 != 0) {
    if (DAT_010a08d0 != '\0') {
      (**(code **)(*(long *)param_1 + 0x6c0))(param_1);
      DAT_010a08d0 = '\0';
    }
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    (**(code **)(*(long *)param_1 + 0xb0))(param_1,DAT_010a08c8);
    DAT_010a08c8 = 0;
  }
  return;
}

~~~
