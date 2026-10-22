# 00bbada8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbada8.md)

## 関数情報

~~~json
{
  "address": "00bbada8",
  "name": "std::logic_error::~logic_error",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c60b6b57d4d493bd61b4f4462d25ea263452212b12277bfdb638d47c3375955f",
  "source_text_sha256": "c60b6b57d4d493bd61b4f4462d25ea263452212b12277bfdb638d47c3375955f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1d60](../00be1/00be1d60.md)

## 疑似コード 1/1 / UTF-8 181 bytes

~~~c

/* std::logic_error::~logic_error() */

void __thiscall std::logic_error::~logic_error(logic_error *this)

{
  ~logic_error(this);
  operator_delete(this);
  return;
}

~~~
