# 007aabac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007aabac",
  "name": "FUN_007aabac",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a89c6d6e39d1ad8e6a0caa702f76e42ba77e14a8f37b305d7254c79a4bcb61c6",
  "source_text_sha256": "a89c6d6e39d1ad8e6a0caa702f76e42ba77e14a8f37b305d7254c79a4bcb61c6"
}
~~~

## 呼び出し元

- [007ac08c](../007ac/007ac08c.md)

## 呼び出し先

- [00aa44c4](../00aa4/00aa44c4.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 440 bytes

~~~c

void FUN_007aabac(undefined8 param_1)

{
  long lVar1;
  ushort local_40 [8];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_40[0] = 0;
  FUN_00aa44c4(0x6c,param_1,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
