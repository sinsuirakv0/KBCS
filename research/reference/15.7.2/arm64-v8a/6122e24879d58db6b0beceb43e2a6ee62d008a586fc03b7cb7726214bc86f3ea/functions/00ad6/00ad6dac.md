# 00ad6dac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ad6dac.md)

## 関数情報

~~~json
{
  "address": "00ad6dac",
  "name": "Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a307a3fd8307d7afd87d9b4d9e77446b35b59d46f200ee495898d3c0a9f3d7e2",
  "source_text_sha256": "a307a3fd8307d7afd87d9b4d9e77446b35b59d46f200ee495898d3c0a9f3d7e2"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"Google サインイン 失敗"
"ンイン 失敗"
~~~
## 疑似コード 1/1 / UTF-8 1303 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void Java_jp_co_ponos_battlecats_MyGoogleSignInListener_onFailure(void)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long *plVar6;
  ulong local_50;
  undefined8 uStack_48;
  undefined8 *local_40;
  undefined4 local_2c;
  long local_28;
  
  plVar6 = DAT_0109fcc0;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fcc0 != (long *)0x0) {
    local_40 = operator_new(0x20);
    uStack_48 = _UNK_002b14c8;
    local_50 = _DAT_002b14c0;
    uVar5 = _UNK_002a7d29;
    uVar4 = _DAT_002a7d14;
    uVar2 = CONCAT35(_DAT_002a7d21,_UNK_002a7d1c);
    uVar3 = CONCAT53(_UNK_002a7d24,_DAT_002a7d21);
    *(undefined1 *)((long)local_40 + 0x1d) = 0;
    local_40[1] = uVar2;
    *local_40 = uVar4;
    *(undefined8 *)((long)local_40 + 0x15) = uVar5;
    *(undefined8 *)((long)local_40 + 0xd) = uVar3;
    local_2c = 0;
    (**(code **)(*plVar6 + 0x30))(plVar6,&local_2c,&local_50);
    if ((local_50 & 1) != 0) {
      operator_delete(local_40);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
