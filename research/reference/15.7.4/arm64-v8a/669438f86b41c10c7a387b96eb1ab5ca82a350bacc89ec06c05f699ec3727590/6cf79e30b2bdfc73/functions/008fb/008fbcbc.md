# 008fbcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](008fbcbc.md)

## 関数情報

~~~json
{
  "address": "008fbcbc",
  "name": "FUN_008fbcbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2",
  "source_text_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2"
}
~~~
## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)
- [00a34cc8](../00a34/00a34cc8.md)

## 呼び出し先

- [008f95c0](../008f9/008f95c0.md)
- [008fb5f4](../008fb/008fb5f4.md)

## 疑似コード 1/1 / UTF-8 268 bytes

~~~c

void FUN_008fbcbc(char *param_1)

{
  if (*param_1 != '\0') {
    if (*(int *)(param_1 + 4) == 1) {
      FUN_008fb5f4(param_1 + 0x18);
      return;
    }
    if (*(int *)(param_1 + 4) == 0) {
      FUN_008f95c0(param_1 + 0x48);
      return;
    }
  }
  return;
}

~~~
