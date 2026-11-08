# 00b7cbec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b7cbec",
  "name": "_ZNSt6__ndk117__assoc_sub_state4waitEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0423d98f7f91e0350ed5ab422fda0df07355d01567184441ca12f8c65aa8b76e",
  "source_text_sha256": "0423d98f7f91e0350ed5ab422fda0df07355d01567184441ca12f8c65aa8b76e"
}
~~~

## 呼び出し元

- [00bdb690](../00bdb/00bdb690.md)

## 呼び出し先

- [00bdb240](../00bdb/00bdb240.md)
- [00bdb250](../00bdb/00bdb250.md)
- [00bdb5e0](../00bdb/00bdb5e0.md)

## 疑似コード / UTF-8 929 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state4waitEv(long *param_1)

{
  long *plVar1;
  uint uVar2;
  long *local_30;
  char local_28;
  
  plVar1 = param_1 + 3;
  local_28 = '\x01';
  local_30 = plVar1;
  _ZNSt6__ndk15mutex4lockEv(plVar1);
  uVar2 = *(uint *)(param_1 + 0xe);
  if ((uVar2 >> 2 & 1) == 0) {
    if ((uVar2 >> 3 & 1) != 0) {
      *(uint *)(param_1 + 0xe) = uVar2 & 0xfffffff3;
      _ZNSt6__ndk15mutex6unlockEv(plVar1);
                    /* WARNING: Could not recover jumptable at 0x00b7cc8c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*param_1 + 0x18))(param_1);
      return;
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,&local_30);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
    if (local_28 == '\0') {
      return;
    }
  }
  _ZNSt6__ndk15mutex6unlockEv(local_30);
  return;
}

~~~
