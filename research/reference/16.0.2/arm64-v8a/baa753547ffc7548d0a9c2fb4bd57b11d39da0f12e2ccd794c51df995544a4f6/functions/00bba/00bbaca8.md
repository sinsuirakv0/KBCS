# 00bbaca8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbac0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0079.md#compare-47e4c92410456f3281f1774ac33e3499)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0091.md#compare-d4a88090898fa3a5d7b0243324a3ea70)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaca8",
  "name": "FUN_00bbaca8",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5203374b575deea6569ec5f8af4b4868c140f578c85489b5ca078e7d986c21a6",
  "source_text_sha256": "5203374b575deea6569ec5f8af4b4868c140f578c85489b5ca078e7d986c21a6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c58190](../00c58/00c58190.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b200](../00c5b/00c5b200.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5d670](../00c5d/00c5d670.md)
- [00c5d6c0](../00c5d/00c5d6c0.md)
- [00c5d6d0](../00c5d/00c5d6d0.md)
- [00c5d720](../00c5d/00c5d720.md)

## 関連文字列（未確認候補）

~~~text
"Reading message file, errno=%d"
"file_descriptor >= 0"
"watch_descriptor >= 0"
~~~

## 疑似コード / UTF-8 1859 bytes

~~~c

undefined8 FUN_00bbaca8(void)

{
  long lVar1;
  int __fd;
  int iVar2;
  long lVar3;
  ssize_t sVar4;
  undefined4 *puVar5;
  char *pcVar6;
  byte *__name;
  undefined1 auStack_180 [12];
  int local_174 [65];
  long local_70;
  
  lVar1 = tpidr_el0;
  local_70 = *(long *)(lVar1 + 0x28);
  _ZN8firebase5Mutex7AcquireEv(&DAT_01126358);
  if (DAT_01126460 == 0) {
    lVar3 = 0;
  }
  else {
    lVar3 = _ZNK8firebase3App7java_vmEv();
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01126358);
  if (lVar3 != 0) {
    __fd = inotify_init();
    if (__fd < 0) {
      pcVar6 = "file_descriptor >= 0";
    }
    else {
      if ((*DAT_01126468 & 1) == 0) {
        __name = DAT_01126468 + 1;
      }
      else {
        __name = *(byte **)(DAT_01126468 + 0x10);
      }
      iVar2 = inotify_add_watch(__fd,(char *)__name,8);
      if (-1 < iVar2) {
        do {
          _ZN8firebase9messaging15ProcessMessagesEv();
          while( true ) {
            sVar4 = read(__fd,auStack_180,0x110);
            _ZN8firebase5Mutex7AcquireEv(&DAT_01126358);
            lVar3 = DAT_01126460;
            _ZN8firebase5Mutex7ReleaseEv(&DAT_01126358);
            if (lVar3 == 0) goto LAB_00bbade4;
            if (sVar4 < 1) break;
            lVar3 = 0;
            do {
              _ZN8firebase9messaging15ProcessMessagesEv();
              lVar3 = (long)((int)lVar3 + *(int *)((long)local_174 + lVar3) + 0x10);
            } while (lVar3 < sVar4);
          }
          puVar5 = (undefined4 *)__errno();
          _ZN8firebase8LogDebugEPKcz("Reading message file, errno=%d",*puVar5);
        } while( true );
      }
      pcVar6 = "watch_descriptor >= 0";
    }
    _ZN8firebase9LogAssertEPKcz(pcVar6);
  }
LAB_00bbade4:
  if (*(long *)(lVar1 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

~~~
