# 00b2aaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b2aaac",
  "name": "FUN_00b2aaac",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "901602ab7ad2721004c5a8d14a1dbd745ed9e8115c746ff441e6601a4a4b95a1",
  "source_text_sha256": "901602ab7ad2721004c5a8d14a1dbd745ed9e8115c746ff441e6601a4a4b95a1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 858 bytes

~~~c

void FUN_00b2aaac(undefined8 *param_1)

{
  long lVar1;
  void *__ptr;
  long lVar2;
  
  lVar1 = param_1[1];
  lVar2 = param_1[2];
  do {
    if (lVar2 == lVar1) {
      if ((void *)*param_1 != (void *)0x0) {
        _ZdlPv((void *)*param_1);
        return;
      }
      return;
    }
    param_1[2] = lVar2 + -0x60;
    if ((*(byte *)(lVar2 + -0x18) & 1) == 0) {
      if ((*(byte *)(lVar2 + -0x30) & 1) == 0) goto LAB_00b2aaec;
LAB_00b2ab08:
      _ZdlPv(*(void **)(lVar2 + -0x20));
      __ptr = *(void **)(lVar2 + -0x48);
    }
    else {
      _ZdlPv(*(void **)(lVar2 + -8));
      if ((*(byte *)(lVar2 + -0x30) & 1) != 0) goto LAB_00b2ab08;
LAB_00b2aaec:
      __ptr = *(void **)(lVar2 + -0x48);
    }
    if (__ptr != (void *)0x0) {
      *(void **)(lVar2 + -0x40) = __ptr;
      _ZdlPv(__ptr);
    }
    lVar2 = param_1[2];
  } while( true );
}

~~~
