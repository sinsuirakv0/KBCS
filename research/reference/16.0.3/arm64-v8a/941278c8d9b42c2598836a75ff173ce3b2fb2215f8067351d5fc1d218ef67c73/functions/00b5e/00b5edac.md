# 00b5edac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b5edac",
  "name": "_ZNK8firebase4Path14FrontDirectoryEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f74ae868b1bd1b2025dafb333c9b7b08b35d28ce2b9e4dcadbd726a00dd08bb",
  "source_text_sha256": "9f74ae868b1bd1b2025dafb333c9b7b08b35d28ce2b9e4dcadbd726a00dd08bb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5cc90](../00c5c/00c5cc90.md)
- [00c5cca0](../00c5c/00c5cca0.md)

## 疑似コード / UTF-8 1331 bytes

~~~c

void _ZNK8firebase4Path14FrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_50;
  byte *local_48;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00b5ee3c:
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
      goto LAB_00b5ee5c;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00b5ee3c;
  _ZNK8firebase4Path14GetDirectoriesEv(&local_50);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  pbVar4 = local_50;
  if (local_50 != (byte *)0x0) {
    if (local_48 != local_50) {
      bVar1 = local_48[-0x18];
      pbVar5 = local_48 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_48 + -8));
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_48 = pbVar3;
      }
    }
    local_48 = pbVar4;
    _ZdlPv(local_50);
  }
LAB_00b5ee5c:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
