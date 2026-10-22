# 00b6afcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b6afcc.md)

## 関数情報

~~~json
{
  "address": "00b6afcc",
  "name": "firebase::auth::PhoneAuthProvider::Listener::~Listener",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5c6e2fca67ddd097b8751c2fd1a71c08dba578d6aeb870d5f10cac53a8f537c",
  "source_text_sha256": "b5c6e2fca67ddd097b8751c2fd1a71c08dba578d6aeb870d5f10cac53a8f537c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bde080](../00bde/00bde080.md)
- [00bde100](../00bde/00bde100.md)
- [00bde2e0](../00bde/00bde2e0.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~
## 疑似コード 1/1 / UTF-8 673 bytes

~~~c

/* firebase::auth::PhoneAuthProvider::Listener::~Listener() */

void __thiscall firebase::auth::PhoneAuthProvider::Listener::~Listener(Listener *this)

{
  App *this_00;
  long *plVar1;
  
  *(undefined **)this = PTR_vtable_00c1bb10 + 0x10;
  this_00 = (App *)app_common::GetAnyApp();
  if (this_00 == (App *)0x0) {
    LogAssert("app != nullptr");
  }
  plVar1 = (long *)App::GetJNIEnv(this_00);
  FUN_00551e14(plVar1,**(undefined8 **)(this + 8),DAT_010a18c0);
  (**(code **)(*plVar1 + 0xb0))(plVar1,**(undefined8 **)(this + 8));
  if (*(void **)(this + 8) != (void *)0x0) {
    operator_delete(*(void **)(this + 8));
    return;
  }
  return;
}

~~~
