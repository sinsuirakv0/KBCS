# 00bbaa5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbaa5c.md)

## 関数情報

~~~json
{
  "address": "00bbaa5c",
  "name": "_ZSt13get_terminatev",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f4d90946841fe0268c523550ba919278bfc578439a8bb9323e8266acd407760",
  "source_text_sha256": "8f4d90946841fe0268c523550ba919278bfc578439a8bb9323e8266acd407760"
}
~~~
## 呼び出し元

- [00be1e10](../00be1/00be1e10.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 107 bytes

~~~c

undefined8 _ZSt13get_terminatev(void)

{
  return *(undefined8 *)PTR___cxa_terminate_handler_00c1c000;
}

~~~
