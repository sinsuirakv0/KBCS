# 00bbbc9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbaca8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-d4a88090898fa3a5d7b0243324a3ea70)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "c845430d15d869623e789724e7b72b02e59097c2c1f3488e6dce4f4c63d59321",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbc9c",
        "00bbbe0f"
      ]
    ],
    "bytes_sha256": "b9fb1768b5dc3b14220d26c3f3ce2087242d458b9b15de22b5c5cdf13507c309",
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbc9c"></a> `00bbbc9c` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbbca0"></a> `00bbbca0` | `fc 6f 12 a9` | stp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbbca4"></a> `00bbbca4` | `fa 67 13 a9` | stp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbbca8"></a> `00bbbca8` | `f8 5f 14 a9` | stp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbbcac"></a> `00bbbcac` | `f6 57 15 a9` | stp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbbcb0"></a> `00bbbcb0` | `f4 4f 16 a9` | stp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbbcb4"></a> `00bbbcb4` | `fd 7b 17 a9` | stp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbbcb8"></a> `00bbbcb8` | `fd c3 05 91` | add x29,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00bbbcbc"></a> `00bbbcbc` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbbcc0"></a> `00bbbcc0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbcc4"></a> `00bbbcc4` | `60 2b 00 90` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbcc8"></a> `00bbbcc8` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbbccc"></a> `00bbbccc` | `a8 03 1a f8` | stur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbbcd0"></a> `00bbbcd0` | `74 7f 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbcd4"></a> `00bbbcd4` | `78 2b 00 90` | adrp x24,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbcd8"></a> `00bbbcd8` | `00 13 42 f9` | ldr x0,[x24, #0x420] | `FALL_THROUGH`
<a id="insn-00bbbcdc"></a> `00bbbcdc` | `80 00 00 b4` | cbz x0,0x00bbbcec | `CONDITIONAL_JUMP`
<a id="insn-00bbbce0"></a> `00bbbce0` | `b0 84 02 94` | bl 0x00c5cfa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbce4"></a> `00bbbce4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbce8"></a> `00bbbce8` | `02 00 00 14` | b 0x00bbbcf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbcec"></a> `00bbbcec` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bbbcf0"></a> `00bbbcf0` | `60 2b 00 90` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbcf4"></a> `00bbbcf4` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbbcf8"></a> `00bbbcf8` | `6e 7f 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbcfc"></a> `00bbbcfc` | `f3 06 00 b4` | cbz x19,0x00bbbdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd00"></a> `00bbbd00` | `68 8a 02 94` | bl 0x00c5e6a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd04"></a> `00bbbd04` | `00 01 f8 37` | tbnz w0,#0x1f,0x00bbbd24 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd08"></a> `00bbbd08` | `68 2b 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbd0c"></a> `00bbbd0c` | `08 15 42 f9` | ldr x8,[x8, #0x428] | `FALL_THROUGH`
<a id="insn-00bbbd10"></a> `00bbbd10` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bbbd14"></a> `00bbbd14` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbbd18"></a> `00bbbd18` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbbd30 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd1c"></a> `00bbbd1c` | `01 05 00 91` | add x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbd20"></a> `00bbbd20` | `05 00 00 14` | b 0x00bbbd34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbd24"></a> `00bbbd24` | `80 b7 ff f0` | adrp x0,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bbbd28"></a> `00bbbd28` | `00 b4 10 91` | add x0,x0,#0x42d | `FALL_THROUGH`
<a id="insn-00bbbd2c"></a> `00bbbd2c` | `2a 00 00 14` | b 0x00bbbdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbd30"></a> `00bbbd30` | `01 09 40 f9` | ldr x1,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbd34"></a> `00bbbd34` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbd38"></a> `00bbbd38` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbbd3c"></a> `00bbbd3c` | `55 8a 02 94` | bl 0x00c5e690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd40"></a> `00bbbd40` | `60 04 f8 37` | tbnz w0,#0x1f,0x00bbbdcc | `CONDITIONAL_JUMP`
<a id="insn-00bbbd44"></a> `00bbbd44` | `74 2b 00 90` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbbd48"></a> `00bbbd48` | `75 b7 ff d0` | adrp x21,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbbd4c"></a> `00bbbd4c` | `f9 03 00 91` | mov x25,sp | `FALL_THROUGH`
<a id="insn-00bbbd50"></a> `00bbbd50` | `94 62 0c 91` | add x20,x20,#0x318 | `FALL_THROUGH`
<a id="insn-00bbbd54"></a> `00bbbd54` | `b5 ca 23 91` | add x21,x21,#0x8f2 | `FALL_THROUGH`
<a id="insn-00bbbd58"></a> `00bbbd58` | `3a 8a 02 94` | bl 0x00c5e640 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd5c"></a> `00bbbd5c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbbd60"></a> `00bbbd60` | `02 22 80 52` | mov w2,#0x110 | `FALL_THROUGH`
<a id="insn-00bbbd64"></a> `00bbbd64` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bbbd68"></a> `00bbbd68` | `62 8a 02 94` | bl 0x00c5e6f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd6c"></a> `00bbbd6c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbbd70"></a> `00bbbd70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbd74"></a> `00bbbd74` | `4b 7f 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd78"></a> `00bbbd78` | `1a 13 42 f9` | ldr x26,[x24, #0x420] | `FALL_THROUGH`
<a id="insn-00bbbd7c"></a> `00bbbd7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbd80"></a> `00bbbd80` | `4c 7f 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd84"></a> `00bbbd84` | `ba 02 00 b4` | cbz x26,0x00bbbdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd88"></a> `00bbbd88` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbd8c"></a> `00bbbd8c` | `6b 01 00 54` | b.lt 0x00bbbdb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd90"></a> `00bbbd90` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbbd94"></a> `00bbbd94` | `3b 03 1a 8b` | add x27,x25,x26 | `FALL_THROUGH`
<a id="insn-00bbbd98"></a> `00bbbd98` | `2a 8a 02 94` | bl 0x00c5e640 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd9c"></a> `00bbbd9c` | `68 0f 40 b9` | ldr w8,[x27, #0xc] | `FALL_THROUGH`
<a id="insn-00bbbda0"></a> `00bbbda0` | `48 03 08 0b` | add w8,w26,w8 | `FALL_THROUGH`
<a id="insn-00bbbda4"></a> `00bbbda4` | `08 41 00 11` | add w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbda8"></a> `00bbbda8` | `1a 7d 40 93` | sxtw x26,w8 | `FALL_THROUGH`
<a id="insn-00bbbdac"></a> `00bbbdac` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00bbbdb0"></a> `00bbbdb0` | `2b ff ff 54` | b.lt 0x00bbbd94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbdb4"></a> `00bbbdb4` | `ea ff ff 17` | b 0x00bbbd5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbdb8"></a> `00bbbdb8` | `ea 74 02 94` | bl 0x00c59160 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdbc"></a> `00bbbdbc` | `01 00 40 b9` | ldr w1,[x0] | `FALL_THROUGH`
<a id="insn-00bbbdc0"></a> `00bbbdc0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbdc4"></a> `00bbbdc4` | `03 81 02 94` | bl 0x00c5c1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdc8"></a> `00bbbdc8` | `e4 ff ff 17` | b 0x00bbbd58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbdcc"></a> `00bbbdcc` | `20 b8 ff 90` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bbbdd0"></a> `00bbbdd0` | `00 04 2a 91` | add x0,x0,#0xa81 | `FALL_THROUGH`
<a id="insn-00bbbdd4"></a> `00bbbdd4` | `b3 80 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdd8"></a> `00bbbdd8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbddc"></a> `00bbbddc` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bbbde0"></a> `00bbbde0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbde4"></a> `00bbbde4` | `41 01 00 54` | b.ne 0x00bbbe0c | `CONDITIONAL_JUMP`
<a id="insn-00bbbde8"></a> `00bbbde8` | `fd 7b 57 a9` | ldp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbbdec"></a> `00bbbdec` | `f4 4f 56 a9` | ldp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbbdf0"></a> `00bbbdf0` | `f6 57 55 a9` | ldp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbbdf4"></a> `00bbbdf4` | `f8 5f 54 a9` | ldp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbbdf8"></a> `00bbbdf8` | `fa 67 53 a9` | ldp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbbdfc"></a> `00bbbdfc` | `fc 6f 52 a9` | ldp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbbe00"></a> `00bbbe00` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbbe04"></a> `00bbbe04` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbbe08"></a> `00bbbe08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbe0c"></a> `00bbbe0c` | `5d 74 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbc9c`](#insn-00bbbc9c) 範囲 `[['00bbbc9c', '00bbbcdf']]`
  - `CONDITIONAL_JUMP` [`00bbbcdc`](#insn-00bbbcdc) → [`00bbbcec`](#insn-00bbbcec)
  - `FALL_THROUGH` [`00bbbcdc`](#insn-00bbbcdc) → [`00bbbce0`](#insn-00bbbce0)
- ブロック [`00bbbce0`](#insn-00bbbce0) 範囲 `[['00bbbce0', '00bbbceb']]`
  - `UNCONDITIONAL_JUMP` [`00bbbce8`](#insn-00bbbce8) → [`00bbbcf0`](#insn-00bbbcf0)
- ブロック [`00bbbcec`](#insn-00bbbcec) 範囲 `[['00bbbcec', '00bbbcef']]`
  - `FALL_THROUGH` [`00bbbcec`](#insn-00bbbcec) → [`00bbbcf0`](#insn-00bbbcf0)
- ブロック [`00bbbcf0`](#insn-00bbbcf0) 範囲 `[['00bbbcf0', '00bbbcff']]`
  - `CONDITIONAL_JUMP` [`00bbbcfc`](#insn-00bbbcfc) → [`00bbbdd8`](#insn-00bbbdd8)
  - `FALL_THROUGH` [`00bbbcfc`](#insn-00bbbcfc) → [`00bbbd00`](#insn-00bbbd00)
- ブロック [`00bbbd00`](#insn-00bbbd00) 範囲 `[['00bbbd00', '00bbbd07']]`
  - `CONDITIONAL_JUMP` [`00bbbd04`](#insn-00bbbd04) → [`00bbbd24`](#insn-00bbbd24)
  - `FALL_THROUGH` [`00bbbd04`](#insn-00bbbd04) → [`00bbbd08`](#insn-00bbbd08)
- ブロック [`00bbbd08`](#insn-00bbbd08) 範囲 `[['00bbbd08', '00bbbd1b']]`
  - `CONDITIONAL_JUMP` [`00bbbd18`](#insn-00bbbd18) → [`00bbbd30`](#insn-00bbbd30)
  - `FALL_THROUGH` [`00bbbd18`](#insn-00bbbd18) → [`00bbbd1c`](#insn-00bbbd1c)
- ブロック [`00bbbd1c`](#insn-00bbbd1c) 範囲 `[['00bbbd1c', '00bbbd23']]`
  - `UNCONDITIONAL_JUMP` [`00bbbd20`](#insn-00bbbd20) → [`00bbbd34`](#insn-00bbbd34)
- ブロック [`00bbbd24`](#insn-00bbbd24) 範囲 `[['00bbbd24', '00bbbd2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbbd2c`](#insn-00bbbd2c) → [`00bbbdd4`](#insn-00bbbdd4)
- ブロック [`00bbbd30`](#insn-00bbbd30) 範囲 `[['00bbbd30', '00bbbd33']]`
  - `FALL_THROUGH` [`00bbbd30`](#insn-00bbbd30) → [`00bbbd34`](#insn-00bbbd34)
- ブロック [`00bbbd34`](#insn-00bbbd34) 範囲 `[['00bbbd34', '00bbbd43']]`
  - `CONDITIONAL_JUMP` [`00bbbd40`](#insn-00bbbd40) → [`00bbbdcc`](#insn-00bbbdcc)
  - `FALL_THROUGH` [`00bbbd40`](#insn-00bbbd40) → [`00bbbd44`](#insn-00bbbd44)
- ブロック [`00bbbd44`](#insn-00bbbd44) 範囲 `[['00bbbd44', '00bbbd57']]`
  - `FALL_THROUGH` [`00bbbd54`](#insn-00bbbd54) → [`00bbbd58`](#insn-00bbbd58)
- ブロック [`00bbbd58`](#insn-00bbbd58) 範囲 `[['00bbbd58', '00bbbd5b']]`
  - `FALL_THROUGH` [`00bbbd58`](#insn-00bbbd58) → [`00bbbd5c`](#insn-00bbbd5c)
- ブロック [`00bbbd5c`](#insn-00bbbd5c) 範囲 `[['00bbbd5c', '00bbbd87']]`
  - `CONDITIONAL_JUMP` [`00bbbd84`](#insn-00bbbd84) → [`00bbbdd8`](#insn-00bbbdd8)
  - `FALL_THROUGH` [`00bbbd84`](#insn-00bbbd84) → [`00bbbd88`](#insn-00bbbd88)
- ブロック [`00bbbd88`](#insn-00bbbd88) 範囲 `[['00bbbd88', '00bbbd8f']]`
  - `CONDITIONAL_JUMP` [`00bbbd8c`](#insn-00bbbd8c) → [`00bbbdb8`](#insn-00bbbdb8)
  - `FALL_THROUGH` [`00bbbd8c`](#insn-00bbbd8c) → [`00bbbd90`](#insn-00bbbd90)
- ブロック [`00bbbd90`](#insn-00bbbd90) 範囲 `[['00bbbd90', '00bbbd93']]`
  - `FALL_THROUGH` [`00bbbd90`](#insn-00bbbd90) → [`00bbbd94`](#insn-00bbbd94)
- ブロック [`00bbbd94`](#insn-00bbbd94) 範囲 `[['00bbbd94', '00bbbdb3']]`
  - `CONDITIONAL_JUMP` [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbd94`](#insn-00bbbd94)
  - `FALL_THROUGH` [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbdb4`](#insn-00bbbdb4)
- ブロック [`00bbbdb4`](#insn-00bbbdb4) 範囲 `[['00bbbdb4', '00bbbdb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbbdb4`](#insn-00bbbdb4) → [`00bbbd5c`](#insn-00bbbd5c)
- ブロック [`00bbbdb8`](#insn-00bbbdb8) 範囲 `[['00bbbdb8', '00bbbdcb']]`
  - `UNCONDITIONAL_JUMP` [`00bbbdc8`](#insn-00bbbdc8) → [`00bbbd58`](#insn-00bbbd58)
- ブロック [`00bbbdcc`](#insn-00bbbdcc) 範囲 `[['00bbbdcc', '00bbbdd3']]`
  - `FALL_THROUGH` [`00bbbdd0`](#insn-00bbbdd0) → [`00bbbdd4`](#insn-00bbbdd4)
- ブロック [`00bbbdd4`](#insn-00bbbdd4) 範囲 `[['00bbbdd4', '00bbbdd7']]`
  - `FALL_THROUGH` [`00bbbdd4`](#insn-00bbbdd4) → [`00bbbdd8`](#insn-00bbbdd8)
- ブロック [`00bbbdd8`](#insn-00bbbdd8) 範囲 `[['00bbbdd8', '00bbbde7']]`
  - `CONDITIONAL_JUMP` [`00bbbde4`](#insn-00bbbde4) → [`00bbbe0c`](#insn-00bbbe0c)
  - `FALL_THROUGH` [`00bbbde4`](#insn-00bbbde4) → [`00bbbde8`](#insn-00bbbde8)
- ブロック [`00bbbde8`](#insn-00bbbde8) 範囲 `[['00bbbde8', '00bbbe0b']]`
- ブロック [`00bbbe0c`](#insn-00bbbe0c) 範囲 `[['00bbbe0c', '00bbbe0f']]`

## 命令位置別の参照

- [`00bbbca0`](#insn-00bbbca0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbca4`](#insn-00bbbca4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbca8`](#insn-00bbbca8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcac`](#insn-00bbbcac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcb0`](#insn-00bbbcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcb4`](#insn-00bbbcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcc8`](#insn-00bbbcc8) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbccc`](#insn-00bbbccc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcd0`](#insn-00bbbcd0) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcd8`](#insn-00bbbcd8) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbcdc`](#insn-00bbbcdc) → [`00bbbcec`](#insn-00bbbcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbce0`](#insn-00bbbce0) → [`00c5cfa0`](../00c5c/00c5cfa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbce8`](#insn-00bbbce8) → [`00bbbcf0`](#insn-00bbbcf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcf4`](#insn-00bbbcf4) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcf8`](#insn-00bbbcf8) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcfc`](#insn-00bbbcfc) → [`00bbbdd8`](#insn-00bbbdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd00`](#insn-00bbbd00) → [`00c5e6a0`](../00c5e/00c5e6a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e6a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd04`](#insn-00bbbd04) → [`00bbbd24`](#insn-00bbbd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd0c`](#insn-00bbbd0c) → `01127428`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbd18`](#insn-00bbbd18) → [`00bbbd30`](#insn-00bbbd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd20`](#insn-00bbbd20) → [`00bbbd34`](#insn-00bbbd34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd28`](#insn-00bbbd28) → `002ae42d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbd2c`](#insn-00bbbd2c) → [`00bbbdd4`](#insn-00bbbdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd3c`](#insn-00bbbd3c) → [`00c5e690`](../00c5e/00c5e690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e690` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd40`](#insn-00bbbd40) → [`00bbbdcc`](#insn-00bbbdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd58`](#insn-00bbbd58) → [`00c5e640`](../00c5e/00c5e640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e640` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd68`](#insn-00bbbd68) → [`00c5e6f0`](../00c5e/00c5e6f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e6f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd70`](#insn-00bbbd70) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd74`](#insn-00bbbd74) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd78`](#insn-00bbbd78) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbd7c`](#insn-00bbbd7c) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd80`](#insn-00bbbd80) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd84`](#insn-00bbbd84) → [`00bbbdd8`](#insn-00bbbdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd8c`](#insn-00bbbd8c) → [`00bbbdb8`](#insn-00bbbdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd98`](#insn-00bbbd98) → [`00c5e640`](../00c5e/00c5e640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e640` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd9c`](#insn-00bbbd9c) → `Stack[-0x174]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbd94`](#insn-00bbbd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb4`](#insn-00bbbdb4) → [`00bbbd5c`](#insn-00bbbd5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb8`](#insn-00bbbdb8) → [`00c59160`](../00c59/00c59160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59160` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdc0`](#insn-00bbbdc0) → `002a98f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbdc4`](#insn-00bbbdc4) → [`00c5c1d0`](../00c5c/00c5c1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdc8`](#insn-00bbbdc8) → [`00bbbd58`](#insn-00bbbd58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdd0`](#insn-00bbbdd0) → `002bfa81`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbdd4`](#insn-00bbbdd4) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbddc`](#insn-00bbbddc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbde4`](#insn-00bbbde4) → [`00bbbe0c`](#insn-00bbbe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbde8`](#insn-00bbbde8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdec`](#insn-00bbbdec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf0`](#insn-00bbbdf0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf4`](#insn-00bbbdf4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf8`](#insn-00bbbdf8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdfc`](#insn-00bbbdfc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe0c`](#insn-00bbbe0c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbca0`](#insn-00bbbca0)

~~~json
{
  "source": "00bbbca0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbca4`](#insn-00bbbca4)

~~~json
{
  "source": "00bbbca4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbca8`](#insn-00bbbca8)

~~~json
{
  "source": "00bbbca8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcac`](#insn-00bbbcac)

~~~json
{
  "source": "00bbbcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcb0`](#insn-00bbbcb0)

~~~json
{
  "source": "00bbbcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcb4`](#insn-00bbbcb4)

~~~json
{
  "source": "00bbbcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcc8`](#insn-00bbbcc8)

~~~json
{
  "source": "00bbbcc8",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbccc`](#insn-00bbbccc)

~~~json
{
  "source": "00bbbccc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcd0`](#insn-00bbbcd0)

~~~json
{
  "source": "00bbbcd0",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbcd8`](#insn-00bbbcd8)

~~~json
{
  "source": "00bbbcd8",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbcdc`](#insn-00bbbcdc)

~~~json
{
  "source": "00bbbcdc",
  "target": "00bbbcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbce0`](#insn-00bbbce0)

~~~json
{
  "source": "00bbbce0",
  "target": "00c5cfa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbce8`](#insn-00bbbce8)

~~~json
{
  "source": "00bbbce8",
  "target": "00bbbcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcf4`](#insn-00bbbcf4)

~~~json
{
  "source": "00bbbcf4",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcf8`](#insn-00bbbcf8)

~~~json
{
  "source": "00bbbcf8",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbcfc`](#insn-00bbbcfc)

~~~json
{
  "source": "00bbbcfc",
  "target": "00bbbdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd00`](#insn-00bbbd00)

~~~json
{
  "source": "00bbbd00",
  "target": "00c5e6a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd04`](#insn-00bbbd04)

~~~json
{
  "source": "00bbbd04",
  "target": "00bbbd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd0c`](#insn-00bbbd0c)

~~~json
{
  "source": "00bbbd0c",
  "target": "01127428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbd18`](#insn-00bbbd18)

~~~json
{
  "source": "00bbbd18",
  "target": "00bbbd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd20`](#insn-00bbbd20)

~~~json
{
  "source": "00bbbd20",
  "target": "00bbbd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd28`](#insn-00bbbd28)

~~~json
{
  "source": "00bbbd28",
  "target": "002ae42d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae42d",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "66696c655f64657363726970746f72203e3d203000",
  "capture_start": "002ae42d",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbd2c`](#insn-00bbbd2c)

~~~json
{
  "source": "00bbbd2c",
  "target": "00bbbdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd3c`](#insn-00bbbd3c)

~~~json
{
  "source": "00bbbd3c",
  "target": "00c5e690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd40`](#insn-00bbbd40)

~~~json
{
  "source": "00bbbd40",
  "target": "00bbbdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd58`](#insn-00bbbd58)

~~~json
{
  "source": "00bbbd58",
  "target": "00c5e640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd68`](#insn-00bbbd68)

~~~json
{
  "source": "00bbbd68",
  "target": "00c5e6f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd70`](#insn-00bbbd70)

~~~json
{
  "source": "00bbbd70",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd74`](#insn-00bbbd74)

~~~json
{
  "source": "00bbbd74",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd78`](#insn-00bbbd78)

~~~json
{
  "source": "00bbbd78",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbd7c`](#insn-00bbbd7c)

~~~json
{
  "source": "00bbbd7c",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd80`](#insn-00bbbd80)

~~~json
{
  "source": "00bbbd80",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd84`](#insn-00bbbd84)

~~~json
{
  "source": "00bbbd84",
  "target": "00bbbdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd8c`](#insn-00bbbd8c)

~~~json
{
  "source": "00bbbd8c",
  "target": "00bbbdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd98`](#insn-00bbbd98)

~~~json
{
  "source": "00bbbd98",
  "target": "00c5e640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd9c`](#insn-00bbbd9c)

~~~json
{
  "source": "00bbbd9c",
  "target": "Stack[-0x174]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdb0`](#insn-00bbbdb0)

~~~json
{
  "source": "00bbbdb0",
  "target": "00bbbd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdb4`](#insn-00bbbdb4)

~~~json
{
  "source": "00bbbdb4",
  "target": "00bbbd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdb8`](#insn-00bbbdb8)

~~~json
{
  "source": "00bbbdb8",
  "target": "00c59160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdc0`](#insn-00bbbdc0)

~~~json
{
  "source": "00bbbdc0",
  "target": "002a98f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98f2",
  "offset": 0,
  "size": 31,
  "datatype": "string",
  "bytes": "52656164696e67206d6573736167652066696c652c206572726e6f3d256400",
  "capture_start": "002a98f2",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbdc4`](#insn-00bbbdc4)

~~~json
{
  "source": "00bbbdc4",
  "target": "00c5c1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdc8`](#insn-00bbbdc8)

~~~json
{
  "source": "00bbbdc8",
  "target": "00bbbd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdd0`](#insn-00bbbdd0)

~~~json
{
  "source": "00bbbdd0",
  "target": "002bfa81",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfa81",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "77617463685f64657363726970746f72203e3d203000",
  "capture_start": "002bfa81",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbdd4`](#insn-00bbbdd4)

~~~json
{
  "source": "00bbbdd4",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbddc`](#insn-00bbbddc)

~~~json
{
  "source": "00bbbddc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbde4`](#insn-00bbbde4)

~~~json
{
  "source": "00bbbde4",
  "target": "00bbbe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbde8`](#insn-00bbbde8)

~~~json
{
  "source": "00bbbde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdec`](#insn-00bbbdec)

~~~json
{
  "source": "00bbbdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdf0`](#insn-00bbbdf0)

~~~json
{
  "source": "00bbbdf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdf4`](#insn-00bbbdf4)

~~~json
{
  "source": "00bbbdf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdf8`](#insn-00bbbdf8)

~~~json
{
  "source": "00bbbdf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdfc`](#insn-00bbbdfc)

~~~json
{
  "source": "00bbbdfc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe0c`](#insn-00bbbe0c)

~~~json
{
  "source": "00bbbe0c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
