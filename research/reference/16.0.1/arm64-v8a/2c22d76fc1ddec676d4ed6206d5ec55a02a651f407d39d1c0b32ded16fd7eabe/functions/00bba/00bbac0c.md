# 00bbac0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bba7e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-b3126bb59f0f6132d09d91b270e67b7f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbaca8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-47e4c92410456f3281f1774ac33e3499)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "2203c3f19a4999cb94362b0ea7674a48b6818d09ed4bf68ba57e17e5710f4aea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbac0c",
        "00bbad7f"
      ]
    ],
    "bytes_sha256": "9f11a2efdaf1e5465541ee9137704c5f30ad77316f44a3fc3a3705b0509069fb",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbac0c"></a> `00bbac0c` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbac10"></a> `00bbac10` | `fc 6f 12 a9` | stp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbac14"></a> `00bbac14` | `fa 67 13 a9` | stp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbac18"></a> `00bbac18` | `f8 5f 14 a9` | stp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbac1c"></a> `00bbac1c` | `f6 57 15 a9` | stp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbac20"></a> `00bbac20` | `f4 4f 16 a9` | stp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbac24"></a> `00bbac24` | `fd 7b 17 a9` | stp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbac28"></a> `00bbac28` | `fd c3 05 91` | add x29,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00bbac2c"></a> `00bbac2c` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbac30"></a> `00bbac30` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbac34"></a> `00bbac34` | `60 2b 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac38"></a> `00bbac38` | `00 60 09 91` | add x0,x0,#0x258 | `FALL_THROUGH`
<a id="insn-00bbac3c"></a> `00bbac3c` | `a8 03 1a f8` | stur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbac40"></a> `00bbac40` | `70 7f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac44"></a> `00bbac44` | `78 2b 00 90` | adrp x24,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac48"></a> `00bbac48` | `00 b3 41 f9` | ldr x0,[x24, #0x360] | `FALL_THROUGH`
<a id="insn-00bbac4c"></a> `00bbac4c` | `80 00 00 b4` | cbz x0,0x00bbac5c | `CONDITIONAL_JUMP`
<a id="insn-00bbac50"></a> `00bbac50` | `ac 84 02 94` | bl 0x00c5bf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac54"></a> `00bbac54` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbac58"></a> `00bbac58` | `02 00 00 14` | b 0x00bbac60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbac5c"></a> `00bbac5c` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bbac60"></a> `00bbac60` | `60 2b 00 90` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac64"></a> `00bbac64` | `00 60 09 91` | add x0,x0,#0x258 | `FALL_THROUGH`
<a id="insn-00bbac68"></a> `00bbac68` | `6a 7f 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac6c"></a> `00bbac6c` | `f3 06 00 b4` | cbz x19,0x00bbad48 | `CONDITIONAL_JUMP`
<a id="insn-00bbac70"></a> `00bbac70` | `64 8a 02 94` | bl 0x00c5d600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac74"></a> `00bbac74` | `00 01 f8 37` | tbnz w0,#0x1f,0x00bbac94 | `CONDITIONAL_JUMP`
<a id="insn-00bbac78"></a> `00bbac78` | `68 2b 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac7c"></a> `00bbac7c` | `08 b5 41 f9` | ldr x8,[x8, #0x368] | `FALL_THROUGH`
<a id="insn-00bbac80"></a> `00bbac80` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bbac84"></a> `00bbac84` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbac88"></a> `00bbac88` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbaca0 | `CONDITIONAL_JUMP`
<a id="insn-00bbac8c"></a> `00bbac8c` | `01 05 00 91` | add x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbac90"></a> `00bbac90` | `05 00 00 14` | b 0x00bbaca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbac94"></a> `00bbac94` | `a0 b7 ff 90` | adrp x0,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bbac98"></a> `00bbac98` | `00 f0 0e 91` | add x0,x0,#0x3bc | `FALL_THROUGH`
<a id="insn-00bbac9c"></a> `00bbac9c` | `2a 00 00 14` | b 0x00bbad44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbaca0"></a> `00bbaca0` | `01 09 40 f9` | ldr x1,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaca4"></a> `00bbaca4` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bbaca8"></a> `00bbaca8` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbacac"></a> `00bbacac` | `51 8a 02 94` | bl 0x00c5d5f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacb0"></a> `00bbacb0` | `60 04 f8 37` | tbnz w0,#0x1f,0x00bbad3c | `CONDITIONAL_JUMP`
<a id="insn-00bbacb4"></a> `00bbacb4` | `74 2b 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbacb8"></a> `00bbacb8` | `75 b7 ff f0` | adrp x21,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbacbc"></a> `00bbacbc` | `f9 03 00 91` | mov x25,sp | `FALL_THROUGH`
<a id="insn-00bbacc0"></a> `00bbacc0` | `94 62 09 91` | add x20,x20,#0x258 | `FALL_THROUGH`
<a id="insn-00bbacc4"></a> `00bbacc4` | `b5 da 1f 91` | add x21,x21,#0x7f6 | `FALL_THROUGH`
<a id="insn-00bbacc8"></a> `00bbacc8` | `36 8a 02 94` | bl 0x00c5d5a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaccc"></a> `00bbaccc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbacd0"></a> `00bbacd0` | `02 22 80 52` | mov w2,#0x110 | `FALL_THROUGH`
<a id="insn-00bbacd4"></a> `00bbacd4` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbacd8"></a> `00bbacd8` | `5e 8a 02 94` | bl 0x00c5d650 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacdc"></a> `00bbacdc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbace0"></a> `00bbace0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `47 7f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbace8"></a> `00bbace8` | `1a b3 41 f9` | ldr x26,[x24, #0x360] | `FALL_THROUGH`
<a id="insn-00bbacec"></a> `00bbacec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbacf0"></a> `00bbacf0` | `48 7f 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacf4"></a> `00bbacf4` | `ba 02 00 b4` | cbz x26,0x00bbad48 | `CONDITIONAL_JUMP`
<a id="insn-00bbacf8"></a> `00bbacf8` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbacfc"></a> `00bbacfc` | `6b 01 00 54` | b.lt 0x00bbad28 | `CONDITIONAL_JUMP`
<a id="insn-00bbad00"></a> `00bbad00` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbad04"></a> `00bbad04` | `3b 03 1a 8b` | add x27,x25,x26 | `FALL_THROUGH`
<a id="insn-00bbad08"></a> `00bbad08` | `26 8a 02 94` | bl 0x00c5d5a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad0c"></a> `00bbad0c` | `68 0f 40 b9` | ldr w8,[x27, #0xc] | `FALL_THROUGH`
<a id="insn-00bbad10"></a> `00bbad10` | `48 03 08 0b` | add w8,w26,w8 | `FALL_THROUGH`
<a id="insn-00bbad14"></a> `00bbad14` | `08 41 00 11` | add w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbad18"></a> `00bbad18` | `1a 7d 40 93` | sxtw x26,w8 | `FALL_THROUGH`
<a id="insn-00bbad1c"></a> `00bbad1c` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00bbad20"></a> `00bbad20` | `2b ff ff 54` | b.lt 0x00bbad04 | `CONDITIONAL_JUMP`
<a id="insn-00bbad24"></a> `00bbad24` | `ea ff ff 17` | b 0x00bbaccc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbad28"></a> `00bbad28` | `e6 74 02 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad2c"></a> `00bbad2c` | `01 00 40 b9` | ldr w1,[x0] | `FALL_THROUGH`
<a id="insn-00bbad30"></a> `00bbad30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbad34"></a> `00bbad34` | `ff 80 02 94` | bl 0x00c5b130 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad38"></a> `00bbad38` | `e4 ff ff 17` | b 0x00bbacc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbad3c"></a> `00bbad3c` | `20 b8 ff b0` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bbad40"></a> `00bbad40` | `00 dc 27 91` | add x0,x0,#0x9f7 | `FALL_THROUGH`
<a id="insn-00bbad44"></a> `00bbad44` | `af 80 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad48"></a> `00bbad48` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbad4c"></a> `00bbad4c` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbad50"></a> `00bbad50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbad54"></a> `00bbad54` | `41 01 00 54` | b.ne 0x00bbad7c | `CONDITIONAL_JUMP`
<a id="insn-00bbad58"></a> `00bbad58` | `fd 7b 57 a9` | ldp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbad5c"></a> `00bbad5c` | `f4 4f 56 a9` | ldp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbad60"></a> `00bbad60` | `f6 57 55 a9` | ldp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbad64"></a> `00bbad64` | `f8 5f 54 a9` | ldp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbad68"></a> `00bbad68` | `fa 67 53 a9` | ldp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbad6c"></a> `00bbad6c` | `fc 6f 52 a9` | ldp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbad70"></a> `00bbad70` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbad74"></a> `00bbad74` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbad78"></a> `00bbad78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbad7c"></a> `00bbad7c` | `59 74 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbac0c`](#insn-00bbac0c) 範囲 `[['00bbac0c', '00bbac4f']]`
  - `CONDITIONAL_JUMP` [`00bbac4c`](#insn-00bbac4c) → [`00bbac5c`](#insn-00bbac5c)
  - `FALL_THROUGH` [`00bbac4c`](#insn-00bbac4c) → [`00bbac50`](#insn-00bbac50)
- ブロック [`00bbac50`](#insn-00bbac50) 範囲 `[['00bbac50', '00bbac5b']]`
  - `UNCONDITIONAL_JUMP` [`00bbac58`](#insn-00bbac58) → [`00bbac60`](#insn-00bbac60)
- ブロック [`00bbac5c`](#insn-00bbac5c) 範囲 `[['00bbac5c', '00bbac5f']]`
  - `FALL_THROUGH` [`00bbac5c`](#insn-00bbac5c) → [`00bbac60`](#insn-00bbac60)
- ブロック [`00bbac60`](#insn-00bbac60) 範囲 `[['00bbac60', '00bbac6f']]`
  - `CONDITIONAL_JUMP` [`00bbac6c`](#insn-00bbac6c) → [`00bbad48`](#insn-00bbad48)
  - `FALL_THROUGH` [`00bbac6c`](#insn-00bbac6c) → [`00bbac70`](#insn-00bbac70)
- ブロック [`00bbac70`](#insn-00bbac70) 範囲 `[['00bbac70', '00bbac77']]`
  - `CONDITIONAL_JUMP` [`00bbac74`](#insn-00bbac74) → [`00bbac94`](#insn-00bbac94)
  - `FALL_THROUGH` [`00bbac74`](#insn-00bbac74) → [`00bbac78`](#insn-00bbac78)
- ブロック [`00bbac78`](#insn-00bbac78) 範囲 `[['00bbac78', '00bbac8b']]`
  - `CONDITIONAL_JUMP` [`00bbac88`](#insn-00bbac88) → [`00bbaca0`](#insn-00bbaca0)
  - `FALL_THROUGH` [`00bbac88`](#insn-00bbac88) → [`00bbac8c`](#insn-00bbac8c)
- ブロック [`00bbac8c`](#insn-00bbac8c) 範囲 `[['00bbac8c', '00bbac93']]`
  - `UNCONDITIONAL_JUMP` [`00bbac90`](#insn-00bbac90) → [`00bbaca4`](#insn-00bbaca4)
- ブロック [`00bbac94`](#insn-00bbac94) 範囲 `[['00bbac94', '00bbac9f']]`
  - `UNCONDITIONAL_JUMP` [`00bbac9c`](#insn-00bbac9c) → [`00bbad44`](#insn-00bbad44)
- ブロック [`00bbaca0`](#insn-00bbaca0) 範囲 `[['00bbaca0', '00bbaca3']]`
  - `FALL_THROUGH` [`00bbaca0`](#insn-00bbaca0) → [`00bbaca4`](#insn-00bbaca4)
- ブロック [`00bbaca4`](#insn-00bbaca4) 範囲 `[['00bbaca4', '00bbacb3']]`
  - `CONDITIONAL_JUMP` [`00bbacb0`](#insn-00bbacb0) → [`00bbad3c`](#insn-00bbad3c)
  - `FALL_THROUGH` [`00bbacb0`](#insn-00bbacb0) → [`00bbacb4`](#insn-00bbacb4)
- ブロック [`00bbacb4`](#insn-00bbacb4) 範囲 `[['00bbacb4', '00bbacc7']]`
  - `FALL_THROUGH` [`00bbacc4`](#insn-00bbacc4) → [`00bbacc8`](#insn-00bbacc8)
- ブロック [`00bbacc8`](#insn-00bbacc8) 範囲 `[['00bbacc8', '00bbaccb']]`
  - `FALL_THROUGH` [`00bbacc8`](#insn-00bbacc8) → [`00bbaccc`](#insn-00bbaccc)
- ブロック [`00bbaccc`](#insn-00bbaccc) 範囲 `[['00bbaccc', '00bbacf7']]`
  - `CONDITIONAL_JUMP` [`00bbacf4`](#insn-00bbacf4) → [`00bbad48`](#insn-00bbad48)
  - `FALL_THROUGH` [`00bbacf4`](#insn-00bbacf4) → [`00bbacf8`](#insn-00bbacf8)
- ブロック [`00bbacf8`](#insn-00bbacf8) 範囲 `[['00bbacf8', '00bbacff']]`
  - `CONDITIONAL_JUMP` [`00bbacfc`](#insn-00bbacfc) → [`00bbad28`](#insn-00bbad28)
  - `FALL_THROUGH` [`00bbacfc`](#insn-00bbacfc) → [`00bbad00`](#insn-00bbad00)
- ブロック [`00bbad00`](#insn-00bbad00) 範囲 `[['00bbad00', '00bbad03']]`
  - `FALL_THROUGH` [`00bbad00`](#insn-00bbad00) → [`00bbad04`](#insn-00bbad04)
- ブロック [`00bbad04`](#insn-00bbad04) 範囲 `[['00bbad04', '00bbad23']]`
  - `CONDITIONAL_JUMP` [`00bbad20`](#insn-00bbad20) → [`00bbad04`](#insn-00bbad04)
  - `FALL_THROUGH` [`00bbad20`](#insn-00bbad20) → [`00bbad24`](#insn-00bbad24)
- ブロック [`00bbad24`](#insn-00bbad24) 範囲 `[['00bbad24', '00bbad27']]`
  - `UNCONDITIONAL_JUMP` [`00bbad24`](#insn-00bbad24) → [`00bbaccc`](#insn-00bbaccc)
- ブロック [`00bbad28`](#insn-00bbad28) 範囲 `[['00bbad28', '00bbad3b']]`
  - `UNCONDITIONAL_JUMP` [`00bbad38`](#insn-00bbad38) → [`00bbacc8`](#insn-00bbacc8)
- ブロック [`00bbad3c`](#insn-00bbad3c) 範囲 `[['00bbad3c', '00bbad43']]`
  - `FALL_THROUGH` [`00bbad40`](#insn-00bbad40) → [`00bbad44`](#insn-00bbad44)
- ブロック [`00bbad44`](#insn-00bbad44) 範囲 `[['00bbad44', '00bbad47']]`
  - `FALL_THROUGH` [`00bbad44`](#insn-00bbad44) → [`00bbad48`](#insn-00bbad48)
- ブロック [`00bbad48`](#insn-00bbad48) 範囲 `[['00bbad48', '00bbad57']]`
  - `CONDITIONAL_JUMP` [`00bbad54`](#insn-00bbad54) → [`00bbad7c`](#insn-00bbad7c)
  - `FALL_THROUGH` [`00bbad54`](#insn-00bbad54) → [`00bbad58`](#insn-00bbad58)
- ブロック [`00bbad58`](#insn-00bbad58) 範囲 `[['00bbad58', '00bbad7b']]`
- ブロック [`00bbad7c`](#insn-00bbad7c) 範囲 `[['00bbad7c', '00bbad7f']]`

## 命令位置別の参照

- [`00bbac10`](#insn-00bbac10) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac14`](#insn-00bbac14) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac18`](#insn-00bbac18) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac1c`](#insn-00bbac1c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac20`](#insn-00bbac20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac24`](#insn-00bbac24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac38`](#insn-00bbac38) → `01126258`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac3c`](#insn-00bbac3c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac40`](#insn-00bbac40) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbac48`](#insn-00bbac48) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac4c`](#insn-00bbac4c) → [`00bbac5c`](#insn-00bbac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac50`](#insn-00bbac50) → [`00c5bf00`](../00c5b/00c5bf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf00` · 推定シンボル `None` · 推定型 `None`
- [`00bbac58`](#insn-00bbac58) → [`00bbac60`](#insn-00bbac60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac64`](#insn-00bbac64) → `01126258`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac68`](#insn-00bbac68) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbac6c`](#insn-00bbac6c) → [`00bbad48`](#insn-00bbad48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac70`](#insn-00bbac70) → [`00c5d600`](../00c5d/00c5d600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d600` · 推定シンボル `None` · 推定型 `None`
- [`00bbac74`](#insn-00bbac74) → [`00bbac94`](#insn-00bbac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac7c`](#insn-00bbac7c) → `01126368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac88`](#insn-00bbac88) → [`00bbaca0`](#insn-00bbaca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac90`](#insn-00bbac90) → [`00bbaca4`](#insn-00bbaca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac98`](#insn-00bbac98) → `002ae3bc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbac9c`](#insn-00bbac9c) → [`00bbad44`](#insn-00bbad44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacac`](#insn-00bbacac) → [`00c5d5f0`](../00c5d/00c5d5f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb0`](#insn-00bbacb0) → [`00bbad3c`](#insn-00bbad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc8`](#insn-00bbacc8) → [`00c5d5a0`](../00c5d/00c5d5a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd8`](#insn-00bbacd8) → [`00c5d650`](../00c5d/00c5d650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d650` · 推定シンボル `None` · 推定型 `None`
- [`00bbace0`](#insn-00bbace0) → `01126258`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbace4`](#insn-00bbace4) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbace8`](#insn-00bbace8) → `01126360`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbacec`](#insn-00bbacec) → `01126258`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf0`](#insn-00bbacf0) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf4`](#insn-00bbacf4) → [`00bbad48`](#insn-00bbad48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacfc`](#insn-00bbacfc) → [`00bbad28`](#insn-00bbad28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad08`](#insn-00bbad08) → [`00c5d5a0`](../00c5d/00c5d5a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad0c`](#insn-00bbad0c) → `Stack[-0x174]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad20`](#insn-00bbad20) → [`00bbad04`](#insn-00bbad04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad24`](#insn-00bbad24) → [`00bbaccc`](#insn-00bbaccc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad28`](#insn-00bbad28) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbad30`](#insn-00bbad30) → `002a97f6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbad34`](#insn-00bbad34) → [`00c5b130`](../00c5b/00c5b130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b130` · 推定シンボル `None` · 推定型 `None`
- [`00bbad38`](#insn-00bbad38) → [`00bbacc8`](#insn-00bbacc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad40`](#insn-00bbad40) → `002bf9f7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbad44`](#insn-00bbad44) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bbad4c`](#insn-00bbad4c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad54`](#insn-00bbad54) → [`00bbad7c`](#insn-00bbad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad58`](#insn-00bbad58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad5c`](#insn-00bbad5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad60`](#insn-00bbad60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad64`](#insn-00bbad64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad68`](#insn-00bbad68) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad6c`](#insn-00bbad6c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad7c`](#insn-00bbad7c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbac10`](#insn-00bbac10)

~~~json
{
  "source": "00bbac10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac14`](#insn-00bbac14)

~~~json
{
  "source": "00bbac14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac18`](#insn-00bbac18)

~~~json
{
  "source": "00bbac18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac1c`](#insn-00bbac1c)

~~~json
{
  "source": "00bbac1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac20`](#insn-00bbac20)

~~~json
{
  "source": "00bbac20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac24`](#insn-00bbac24)

~~~json
{
  "source": "00bbac24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac38`](#insn-00bbac38)

~~~json
{
  "source": "00bbac38",
  "target": "01126258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac3c`](#insn-00bbac3c)

~~~json
{
  "source": "00bbac3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac40`](#insn-00bbac40)

~~~json
{
  "source": "00bbac40",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac48`](#insn-00bbac48)

~~~json
{
  "source": "00bbac48",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac4c`](#insn-00bbac4c)

~~~json
{
  "source": "00bbac4c",
  "target": "00bbac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac50`](#insn-00bbac50)

~~~json
{
  "source": "00bbac50",
  "target": "00c5bf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac58`](#insn-00bbac58)

~~~json
{
  "source": "00bbac58",
  "target": "00bbac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac64`](#insn-00bbac64)

~~~json
{
  "source": "00bbac64",
  "target": "01126258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac68`](#insn-00bbac68)

~~~json
{
  "source": "00bbac68",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac6c`](#insn-00bbac6c)

~~~json
{
  "source": "00bbac6c",
  "target": "00bbad48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac70`](#insn-00bbac70)

~~~json
{
  "source": "00bbac70",
  "target": "00c5d600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac74`](#insn-00bbac74)

~~~json
{
  "source": "00bbac74",
  "target": "00bbac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac7c`](#insn-00bbac7c)

~~~json
{
  "source": "00bbac7c",
  "target": "01126368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126368",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac88`](#insn-00bbac88)

~~~json
{
  "source": "00bbac88",
  "target": "00bbaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac90`](#insn-00bbac90)

~~~json
{
  "source": "00bbac90",
  "target": "00bbaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac98`](#insn-00bbac98)

~~~json
{
  "source": "00bbac98",
  "target": "002ae3bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae3bc",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "66696c655f64657363726970746f72203e3d203000",
  "capture_start": "002ae3bc",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbac9c`](#insn-00bbac9c)

~~~json
{
  "source": "00bbac9c",
  "target": "00bbad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacac`](#insn-00bbacac)

~~~json
{
  "source": "00bbacac",
  "target": "00c5d5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "00bbad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc8`](#insn-00bbacc8)

~~~json
{
  "source": "00bbacc8",
  "target": "00c5d5a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacd8`](#insn-00bbacd8)

~~~json
{
  "source": "00bbacd8",
  "target": "00c5d650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbace0`](#insn-00bbace0)

~~~json
{
  "source": "00bbace0",
  "target": "01126258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbace4`](#insn-00bbace4)

~~~json
{
  "source": "00bbace4",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbace8`](#insn-00bbace8)

~~~json
{
  "source": "00bbace8",
  "target": "01126360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126360",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbacec`](#insn-00bbacec)

~~~json
{
  "source": "00bbacec",
  "target": "01126258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacf0`](#insn-00bbacf0)

~~~json
{
  "source": "00bbacf0",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacf4`](#insn-00bbacf4)

~~~json
{
  "source": "00bbacf4",
  "target": "00bbad48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacfc`](#insn-00bbacfc)

~~~json
{
  "source": "00bbacfc",
  "target": "00bbad28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad08`](#insn-00bbad08)

~~~json
{
  "source": "00bbad08",
  "target": "00c5d5a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad0c`](#insn-00bbad0c)

~~~json
{
  "source": "00bbad0c",
  "target": "Stack[-0x174]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad20`](#insn-00bbad20)

~~~json
{
  "source": "00bbad20",
  "target": "00bbad04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad24`](#insn-00bbad24)

~~~json
{
  "source": "00bbad24",
  "target": "00bbaccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad28`](#insn-00bbad28)

~~~json
{
  "source": "00bbad28",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad30`](#insn-00bbad30)

~~~json
{
  "source": "00bbad30",
  "target": "002a97f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a97f6",
  "offset": 0,
  "size": 31,
  "datatype": "string",
  "bytes": "52656164696e67206d6573736167652066696c652c206572726e6f3d256400",
  "capture_start": "002a97f6",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbad34`](#insn-00bbad34)

~~~json
{
  "source": "00bbad34",
  "target": "00c5b130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad38`](#insn-00bbad38)

~~~json
{
  "source": "00bbad38",
  "target": "00bbacc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad40`](#insn-00bbad40)

~~~json
{
  "source": "00bbad40",
  "target": "002bf9f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf9f7",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "77617463685f64657363726970746f72203e3d203000",
  "capture_start": "002bf9f7",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbad44`](#insn-00bbad44)

~~~json
{
  "source": "00bbad44",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad4c`](#insn-00bbad4c)

~~~json
{
  "source": "00bbad4c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad54`](#insn-00bbad54)

~~~json
{
  "source": "00bbad54",
  "target": "00bbad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad58`](#insn-00bbad58)

~~~json
{
  "source": "00bbad58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad5c`](#insn-00bbad5c)

~~~json
{
  "source": "00bbad5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad60`](#insn-00bbad60)

~~~json
{
  "source": "00bbad60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad64`](#insn-00bbad64)

~~~json
{
  "source": "00bbad64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad68`](#insn-00bbad68)

~~~json
{
  "source": "00bbad68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad6c`](#insn-00bbad6c)

~~~json
{
  "source": "00bbad6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad7c`](#insn-00bbad7c)

~~~json
{
  "source": "00bbad7c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
