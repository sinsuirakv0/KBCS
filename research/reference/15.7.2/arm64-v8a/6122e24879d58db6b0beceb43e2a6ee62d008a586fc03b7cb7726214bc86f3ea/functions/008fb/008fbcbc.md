# 008fbcbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "0f4de6a988ec9c84d72e183051da84ca2d0c0d675dd3a2d60ee160557e889ee3",
  "source_text_sha256": "0f4de6a988ec9c84d72e183051da84ca2d0c0d675dd3a2d60ee160557e889ee3"
}
~~~
## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)
- [00a34c84](../00a34/00a34c84.md)

## 呼び出し先

- [008f95c0](../008f9/008f95c0.md)
- [008fb5f4](../008fb/008fb5f4.md)

## 疑似コード 1/1 / UTF-8 285 bytes

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
