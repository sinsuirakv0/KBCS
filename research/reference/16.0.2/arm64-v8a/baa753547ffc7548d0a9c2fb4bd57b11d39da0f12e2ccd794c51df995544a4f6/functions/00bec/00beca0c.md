# 00beca0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00beca0c",
  "name": "FUN_00beca0c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bca8ad55d8cb5cc8909fb6a58e1eaa2186fa6a692888727ccfa1a89ecdbd8301",
  "source_text_sha256": "bca8ad55d8cb5cc8909fb6a58e1eaa2186fa6a692888727ccfa1a89ecdbd8301"
}
~~~

## 呼び出し元

- [00be5c64](../00be5/00be5c64.md)
- [00bec76c](../00bec/00bec76c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1481 bytes

~~~c

void FUN_00beca0c(long *param_1,long *param_2,long *param_3,long *param_4,long *param_5)

{
  long lVar1;
  long lVar2;
  long lVar3;
  
  lVar1 = *param_2;
  lVar2 = *param_1;
  lVar3 = *param_3;
  if (lVar1 < lVar2) {
    if (lVar3 < lVar1) {
      *param_1 = lVar3;
    }
    else {
      *param_1 = lVar1;
      *param_2 = lVar2;
      lVar3 = *param_3;
      if (lVar2 <= lVar3) goto LAB_00beca8c;
      *param_2 = lVar3;
    }
    *param_3 = lVar2;
    lVar3 = lVar2;
  }
  else if (lVar3 < lVar1) {
    *param_2 = lVar3;
    *param_3 = lVar1;
    lVar2 = *param_1;
    lVar3 = lVar1;
    if (*param_2 < lVar2) {
      *param_1 = *param_2;
      *param_2 = lVar2;
      lVar3 = *param_3;
    }
  }
LAB_00beca8c:
  if (*param_4 < lVar3) {
    *param_3 = *param_4;
    *param_4 = lVar3;
    lVar3 = *param_2;
    if (*param_3 < lVar3) {
      *param_2 = *param_3;
      *param_3 = lVar3;
      lVar3 = *param_1;
      if (*param_2 < lVar3) {
        *param_1 = *param_2;
        *param_2 = lVar3;
      }
    }
  }
  lVar3 = *param_4;
  if (*param_5 < lVar3) {
    *param_4 = *param_5;
    *param_5 = lVar3;
    lVar3 = *param_3;
    if (*param_4 < lVar3) {
      *param_3 = *param_4;
      *param_4 = lVar3;
      lVar3 = *param_2;
      if (*param_3 < lVar3) {
        *param_2 = *param_3;
        *param_3 = lVar3;
        lVar3 = *param_1;
        if (*param_2 < lVar3) {
          *param_1 = *param_2;
          *param_2 = lVar3;
        }
      }
    }
  }
  return;
}

~~~
