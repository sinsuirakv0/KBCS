# 00bbbc9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbbc9c",
  "name": "FUN_00bbbc9c",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c845430d15d869623e789724e7b72b02e59097c2c1f3488e6dce4f4c63d59321",
  "source_text_sha256": "c845430d15d869623e789724e7b72b02e59097c2c1f3488e6dce4f4c63d59321"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c59160](../00c59/00c59160.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c1d0](../00c5c/00c5c1d0.md)
- [00c5cfa0](../00c5c/00c5cfa0.md)
- [00c5e640](../00c5e/00c5e640.md)
- [00c5e690](../00c5e/00c5e690.md)
- [00c5e6a0](../00c5e/00c5e6a0.md)
- [00c5e6f0](../00c5e/00c5e6f0.md)

## 関連文字列（未確認候補）

~~~text
"Reading message file, errno=%d"
"file_descriptor >= 0"
"watch_descriptor >= 0"
~~~

## 疑似コード / UTF-8 1859 bytes

~~~c

undefined8 FUN_00bbbc9c(void)

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
  _ZN8firebase5Mutex7AcquireEv(&DAT_01127318);
  if (DAT_01127420 == 0) {
    lVar3 = 0;
  }
  else {
    lVar3 = _ZNK8firebase3App7java_vmEv();
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01127318);
  if (lVar3 != 0) {
    __fd = inotify_init();
    if (__fd < 0) {
      pcVar6 = "file_descriptor >= 0";
    }
    else {
      if ((*DAT_01127428 & 1) == 0) {
        __name = DAT_01127428 + 1;
      }
      else {
        __name = *(byte **)(DAT_01127428 + 0x10);
      }
      iVar2 = inotify_add_watch(__fd,(char *)__name,8);
      if (-1 < iVar2) {
        do {
          _ZN8firebase9messaging15ProcessMessagesEv();
          while( true ) {
            sVar4 = read(__fd,auStack_180,0x110);
            _ZN8firebase5Mutex7AcquireEv(&DAT_01127318);
            lVar3 = DAT_01127420;
            _ZN8firebase5Mutex7ReleaseEv(&DAT_01127318);
            if (lVar3 == 0) goto LAB_00bbbdd8;
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
LAB_00bbbdd8:
  if (*(long *)(lVar1 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

~~~
