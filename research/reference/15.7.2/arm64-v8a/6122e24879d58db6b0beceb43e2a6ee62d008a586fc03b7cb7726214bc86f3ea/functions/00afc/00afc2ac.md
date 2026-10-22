# 00afc2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afc2ac.md)

## 関数情報

~~~json
{
  "address": "00afc2ac",
  "name": "firebase::callback::BlockingCallback::~BlockingCallback",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b94b99d66dec6ae502a4ae9180ee2d7016134b65243ba74de5e3069d684fa918",
  "source_text_sha256": "b94b99d66dec6ae502a4ae9180ee2d7016134b65243ba74de5e3069d684fa918"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdebc0](../00bde/00bdebc0.md)

## 疑似コード 1/1 / UTF-8 571 bytes

~~~c

/* firebase::callback::BlockingCallback::~BlockingCallback() */

void __thiscall firebase::callback::BlockingCallback::~BlockingCallback(BlockingCallback *this)

{
  *(undefined **)this = PTR_vtable_00c1b880 + 0x10;
  sem_post((sem_t *)**(undefined8 **)(this + 0x10));
  if (*(long **)(this + 8) != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00afc2f0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(**(long **)(this + 8) + 8))();
    return;
  }
  return;
}

~~~
