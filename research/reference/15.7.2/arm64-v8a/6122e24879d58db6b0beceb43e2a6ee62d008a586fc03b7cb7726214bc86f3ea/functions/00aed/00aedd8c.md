# 00aedd8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aedd8c.md)

## 関数情報

~~~json
{
  "address": "00aedd8c",
  "name": "firebase::util::uri::CacheMethodIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd5d2def12316c61bad260ed344cbce4863ccccb84a7c50bfde0c64cb64540f",
  "source_text_sha256": "6fd5d2def12316c61bad260ed344cbce4863ccccb84a7c50bfde0c64cb64540f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~
## 疑似コード 1/1 / UTF-8 459 bytes

~~~c

/* firebase::util::uri::CacheMethodIds(_JNIEnv*, _jobject*) */

void firebase::util::uri::CacheMethodIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0960 == (_jclass *)0x0) {
    DAT_010a0960 = (_jclass *)FindClassGlobal(param_1,param_2,0,"android/net/Uri",0);
  }
  LookupMethodIds(param_1,DAT_010a0960,(MethodNameSignature *)&PTR_s_toString_00c10540,2,
                  (_jmethodID **)&DAT_010a0970,"android/net/Uri");
  return;
}

~~~
