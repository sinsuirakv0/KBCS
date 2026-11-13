# 00acbaf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acbaf8",
  "name": "FUN_00acbaf8",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2512a58ea2d267998fb5ca3a8e5a12c69edc909918dd513010f0184c4314ced0",
  "source_text_sha256": "2512a58ea2d267998fb5ca3a8e5a12c69edc909918dd513010f0184c4314ced0"
}
~~~

## 呼び出し元

- [00731fc4](../00731/00731fc4.md)
- [00732020](../00732/00732020.md)
- [009359a4](../00935/009359a4.md)
- [00935a30](../00935/00935a30.md)
- [00acc088](../00acc/00acc088.md)
- [00acc0e8](../00acc/00acc0e8.md)

## 呼び出し先

- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 1049 bytes

~~~c

void FUN_00acbaf8(undefined8 *param_1)

{
  void *__ptr;
  long lVar1;
  long *plVar2;
  void *pvVar3;
  void *pvVar4;
  
  pvVar3 = (void *)param_1[8];
  *param_1 = &PTR_FUN_00c8d990;
  if (pvVar3 != (void *)0x0) {
    pvVar4 = (void *)param_1[9];
    __ptr = pvVar3;
    if (pvVar4 != pvVar3) {
      do {
        plVar2 = *(long **)((long)pvVar4 + -8);
        if ((plVar2 != (long *)0x0) &&
           (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0)) {
          (**(code **)(*plVar2 + 0x10))(plVar2);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
        }
        pvVar4 = (void *)((long)pvVar4 + -0x10);
      } while (pvVar4 != pvVar3);
      __ptr = (void *)param_1[8];
    }
    param_1[9] = pvVar3;
    _ZdlPv(__ptr);
  }
  plVar2 = (long *)param_1[7];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~
