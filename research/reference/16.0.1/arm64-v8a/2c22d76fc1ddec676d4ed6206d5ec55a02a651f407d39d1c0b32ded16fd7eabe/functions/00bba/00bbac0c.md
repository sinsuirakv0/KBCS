# 00bbac0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbac0c",
  "name": "FUN_00bbac0c",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2203c3f19a4999cb94362b0ea7674a48b6818d09ed4bf68ba57e17e5710f4aea",
  "source_text_sha256": "2203c3f19a4999cb94362b0ea7674a48b6818d09ed4bf68ba57e17e5710f4aea"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b130](../00c5b/00c5b130.md)
- [00c5bf00](../00c5b/00c5bf00.md)
- [00c5d5a0](../00c5d/00c5d5a0.md)
- [00c5d5f0](../00c5d/00c5d5f0.md)
- [00c5d600](../00c5d/00c5d600.md)
- [00c5d650](../00c5d/00c5d650.md)

## 関連文字列（未確認候補）

~~~text
"Reading message file, errno=%d"
"file_descriptor >= 0"
"watch_descriptor >= 0"
~~~

## 疑似コード / UTF-8 1859 bytes

~~~c

undefined8 FUN_00bbac0c(void)

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
  _ZN8firebase5Mutex7AcquireEv(&DAT_01126258);
  if (DAT_01126360 == 0) {
    lVar3 = 0;
  }
  else {
    lVar3 = _ZNK8firebase3App7java_vmEv();
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01126258);
  if (lVar3 != 0) {
    __fd = inotify_init();
    if (__fd < 0) {
      pcVar6 = "file_descriptor >= 0";
    }
    else {
      if ((*DAT_01126368 & 1) == 0) {
        __name = DAT_01126368 + 1;
      }
      else {
        __name = *(byte **)(DAT_01126368 + 0x10);
      }
      iVar2 = inotify_add_watch(__fd,(char *)__name,8);
      if (-1 < iVar2) {
        do {
          _ZN8firebase9messaging15ProcessMessagesEv();
          while( true ) {
            sVar4 = read(__fd,auStack_180,0x110);
            _ZN8firebase5Mutex7AcquireEv(&DAT_01126258);
            lVar3 = DAT_01126360;
            _ZN8firebase5Mutex7ReleaseEv(&DAT_01126258);
            if (lVar3 == 0) goto LAB_00bbad48;
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
LAB_00bbad48:
  if (*(long *)(lVar1 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

~~~
