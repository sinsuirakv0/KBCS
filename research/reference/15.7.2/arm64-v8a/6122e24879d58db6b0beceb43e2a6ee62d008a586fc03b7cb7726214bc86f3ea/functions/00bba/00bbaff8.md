# 00bbaff8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaff8.md)

## 関数情報

~~~json
{
  "address": "00bbaff8",
  "name": "std::bad_cast::~bad_cast",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5edaad7d60fbfdbe999e0ff99cfd35b46130faab9fea3ae866bf99f32e72a7d8",
  "source_text_sha256": "5edaad7d60fbfdbe999e0ff99cfd35b46130faab9fea3ae866bf99f32e72a7d8"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1390](../00be1/00be1390.md)

## 疑似コード 1/1 / UTF-8 163 bytes

~~~c

/* std::bad_cast::~bad_cast() */

void __thiscall std::bad_cast::~bad_cast(bad_cast *this)

{
  ~bad_cast(this);
  operator_delete(this);
  return;
}

~~~
