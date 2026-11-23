# 00ac9ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ac9d14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-6d5fb2fbd097f47883c24c3b981a46a9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ac9e20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9e20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-ade99bf36843d3c66aeb22dd21ba099c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9ddc",
  "name": "FUN_00ac9ddc",
  "size": 404,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d7855ba7d8070d250650f55e7d6b82d0ec8a2a604b174b6217bdf6133d2a22cf",
  "source_text_sha256": "d7855ba7d8070d250650f55e7d6b82d0ec8a2a604b174b6217bdf6133d2a22cf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9ddc",
        "00ac9f6f"
      ]
    ],
    "bytes_sha256": "185f23115f7ea96d814f20b6c8775bebcfb9227878bed089d0bc7218a5a2986e",
    "instruction_count": 101,
    "instruction_bytes": 404,
    "body_bytes": 404,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ab3400](../00ab3/00ab3400.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00ac9f70](../00ac9/00ac9f70.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb1f0](../00bdb/00bdb1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1617 bytes

~~~c

void FUN_00ac9ddc(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  void *__src;
  size_t sVar4;
  void *pvVar5;
  size_t __n;
  
  pvVar5 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar5 >> 6) * -0x5555555555555555) < param_2) {
    __src = (void *)*param_1;
    sVar4 = (long)pvVar5 - (long)__src;
    uVar1 = ((long)sVar4 >> 6) * -0x5555555555555555 + param_2;
    if (0x155555555555555 < uVar1) {
      FUN_00ac9f70(param_1);
LAB_00ac9f6c:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar2 = param_1[2] - (long)__src >> 6;
    uVar3 = lVar2 * 0x5555555555555556;
    if (uVar3 < uVar1 || uVar3 - uVar1 == 0) {
      uVar3 = uVar1;
    }
    if (0xaaaaaaaaaaaaa9 < (ulong)(lVar2 * -0x5555555555555555)) {
      uVar3 = 0x155555555555555;
    }
    if (uVar3 == 0) {
      lVar2 = 0;
    }
    else {
      if (0x155555555555555 < uVar3) goto LAB_00ac9f6c;
      lVar2 = _Znwm(uVar3 * 0xc0);
    }
    pvVar5 = (void *)(lVar2 + ((long)sVar4 >> 6) * 0x40);
    __n = ((param_2 * 0xc0 - 0xc0) / 0xc0) * 0xc0 + 0xc0;
    memset(pvVar5,0,__n);
    memcpy((void *)((long)pvVar5 - sVar4),__src,sVar4);
    *param_1 = (void *)((long)pvVar5 - sVar4);
    param_1[1] = (long)pvVar5 + __n;
    param_1[2] = lVar2 + uVar3 * 0xc0;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar4 = ((param_2 * 0xc0 - 0xc0) / 0xc0) * 0xc0 + 0xc0;
      memset(pvVar5,0,sVar4);
      pvVar5 = (void *)((long)pvVar5 + sVar4);
    }
    param_1[1] = pvVar5;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac9ddc"></a> `00ac9ddc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ac9de0"></a> `00ac9de0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9de4"></a> `00ac9de4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9de8"></a> `00ac9de8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9dec"></a> `00ac9dec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9df0"></a> `00ac9df0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac9df4"></a> `00ac9df4` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9df8"></a> `00ac9df8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac9dfc"></a> `00ac9dfc` | `09 01 15 cb` | sub x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00ac9e00"></a> `00ac9e00` | `2a fd 46 93` | asr x10,x9,#0x6 | `FALL_THROUGH`
<a id="insn-00ac9e04"></a> `00ac9e04` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ac9e08"></a> `00ac9e08` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00ac9e0c"></a> `00ac9e0c` | `4a 7d 09 9b` | mul x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9e10"></a> `00ac9e10` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00ac9e14"></a> `00ac9e14` | `e2 03 00 54` | b.cs 0x00ac9e90 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e18"></a> `00ac9e18` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00ac9e1c"></a> `00ac9e1c` | `b5 02 14 cb` | sub x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9e20"></a> `00ac9e20` | `aa fe 46 93` | asr x10,x21,#0x6 | `FALL_THROUGH`
<a id="insn-00ac9e24"></a> `00ac9e24` | `56 7d 09 9b` | mul x22,x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9e28"></a> `00ac9e28` | `e9 f3 00 b2` | orr x9,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00ac9e2c"></a> `00ac9e2c` | `a9 2a e0 f2` | movk x9,#0x155, LSL #48 | `FALL_THROUGH`
<a id="insn-00ac9e30"></a> `00ac9e30` | `ca 02 01 8b` | add x10,x22,x1 | `FALL_THROUGH`
<a id="insn-00ac9e34"></a> `00ac9e34` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9e38"></a> `00ac9e38` | `68 09 00 54` | b.hi 0x00ac9f64 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e3c"></a> `00ac9e3c` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00ac9e40"></a> `00ac9e40` | `f7 f3 01 b2` | orr x23,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ac9e44"></a> `00ac9e44` | `ec f3 01 b2` | orr x12,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ac9e48"></a> `00ac9e48` | `08 fd 46 93` | asr x8,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00ac9e4c"></a> `00ac9e4c` | `77 55 95 f2` | movk x23,#0xaaab | `FALL_THROUGH`
<a id="insn-00ac9e50"></a> `00ac9e50` | `4c 15 e0 f2` | movk x12,#0xaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00ac9e54"></a> `00ac9e54` | `08 7d 17 9b` | mul x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00ac9e58"></a> `00ac9e58` | `0b f9 7f d3` | lsl x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9e5c"></a> `00ac9e5c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00ac9e60"></a> `00ac9e60` | `6a 81 8a 9a` | csel x10,x11,x10,hi | `FALL_THROUGH`
<a id="insn-00ac9e64"></a> `00ac9e64` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00ac9e68"></a> `00ac9e68` | `58 31 89 9a` | csel x24,x10,x9,cc | `FALL_THROUGH`
<a id="insn-00ac9e6c"></a> `00ac9e6c` | `58 03 00 b4` | cbz x24,0x00ac9ed4 | `CONDITIONAL_JUMP`
<a id="insn-00ac9e70"></a> `00ac9e70` | `1f 03 09 eb` | cmp x24,x9 | `FALL_THROUGH`
<a id="insn-00ac9e74"></a> `00ac9e74` | `c8 07 00 54` | b.hi 0x00ac9f6c | `CONDITIONAL_JUMP`
<a id="insn-00ac9e78"></a> `00ac9e78` | `08 07 18 8b` | add x8,x24,x24, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ac9e7c"></a> `00ac9e7c` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00ac9e80"></a> `00ac9e80` | `00 e5 7a d3` | lsl x0,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00ac9e84"></a> `00ac9e84` | `5b 44 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9e88"></a> `00ac9e88` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00ac9e8c"></a> `00ac9e8c` | `13 00 00 14` | b 0x00ac9ed8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9e90"></a> `00ac9e90` | `e1 01 00 b4` | cbz x1,0x00ac9ecc | `CONDITIONAL_JUMP`
<a id="insn-00ac9e94"></a> `00ac9e94` | `08 18 80 52` | mov w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00ac9e98"></a> `00ac9e98` | `e9 17 80 92` | mov x9,#-0xc0 | `FALL_THROUGH`
<a id="insn-00ac9e9c"></a> `00ac9e9c` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ac9ea0"></a> `00ac9ea0` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9ea4"></a> `00ac9ea4` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00ac9ea8"></a> `00ac9ea8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9eac"></a> `00ac9eac` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9eb0"></a> `00ac9eb0` | `29 7d ca 9b` | umulh x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ac9eb4"></a> `00ac9eb4` | `0a 18 80 d2` | mov x10,#0xc0 | `FALL_THROUGH`
<a id="insn-00ac9eb8"></a> `00ac9eb8` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ac9ebc"></a> `00ac9ebc` | `34 29 08 9b` | madd x20,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00ac9ec0"></a> `00ac9ec0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ac9ec4"></a> `00ac9ec4` | `cb 44 04 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9ec8"></a> `00ac9ec8` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9ecc"></a> `00ac9ecc` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9ed0"></a> `00ac9ed0` | `1f 00 00 14` | b 0x00ac9f4c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9ed4"></a> `00ac9ed4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00ac9ed8"></a> `00ac9ed8` | `08 18 80 52` | mov w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00ac9edc"></a> `00ac9edc` | `e9 17 80 92` | mov x9,#-0xc0 | `FALL_THROUGH`
<a id="insn-00ac9ee0"></a> `00ac9ee0` | `0a 18 80 d2` | mov x10,#0xc0 | `FALL_THROUGH`
<a id="insn-00ac9ee4"></a> `00ac9ee4` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9ee8"></a> `00ac9ee8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9eec"></a> `00ac9eec` | `d6 02 08 9b` | madd x22,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00ac9ef0"></a> `00ac9ef0` | `18 03 08 9b` | madd x24,x24,x8,x0 | `FALL_THROUGH`
<a id="insn-00ac9ef4"></a> `00ac9ef4` | `29 7d d7 9b` | umulh x9,x9,x23 | `FALL_THROUGH`
<a id="insn-00ac9ef8"></a> `00ac9ef8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9efc"></a> `00ac9efc` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ac9f00"></a> `00ac9f00` | `37 29 08 9b` | madd x23,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00ac9f04"></a> `00ac9f04` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00ac9f08"></a> `00ac9f08` | `ba 44 04 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9f0c"></a> `00ac9f0c` | `d7 02 17 8b` | add x23,x22,x23 | `FALL_THROUGH`
<a id="insn-00ac9f10"></a> `00ac9f10` | `d6 02 15 cb` | sub x22,x22,x21 | `FALL_THROUGH`
<a id="insn-00ac9f14"></a> `00ac9f14` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ac9f18"></a> `00ac9f18` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9f1c"></a> `00ac9f1c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ac9f20"></a> `00ac9f20` | `90 44 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9f24"></a> `00ac9f24` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00ac9f28"></a> `00ac9f28` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9f2c"></a> `00ac9f2c` | `14 01 00 b4` | cbz x20,0x00ac9f4c | `CONDITIONAL_JUMP`
<a id="insn-00ac9f30"></a> `00ac9f30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac9f34"></a> `00ac9f34` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9f38"></a> `00ac9f38` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9f3c"></a> `00ac9f3c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9f40"></a> `00ac9f40` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9f44"></a> `00ac9f44` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9f48"></a> `00ac9f48` | `32 44 04 14` | b 0x00bdb010 | `CALL_TERMINATOR`
<a id="insn-00ac9f4c"></a> `00ac9f4c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9f50"></a> `00ac9f50` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9f54"></a> `00ac9f54` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9f58"></a> `00ac9f58` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9f5c"></a> `00ac9f5c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ac9f60"></a> `00ac9f60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac9f64"></a> `00ac9f64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac9f68"></a> `00ac9f68` | `02 00 00 94` | bl 0x00ac9f70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9f6c"></a> `00ac9f6c` | `05 51 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9ddc`](#insn-00ac9ddc) 範囲 `[['00ac9ddc', '00ac9e17']]`
  - `CONDITIONAL_JUMP` [`00ac9e14`](#insn-00ac9e14) → [`00ac9e90`](#insn-00ac9e90)
  - `FALL_THROUGH` [`00ac9e14`](#insn-00ac9e14) → [`00ac9e18`](#insn-00ac9e18)
- ブロック [`00ac9e18`](#insn-00ac9e18) 範囲 `[['00ac9e18', '00ac9e3b']]`
  - `CONDITIONAL_JUMP` [`00ac9e38`](#insn-00ac9e38) → [`00ac9f64`](#insn-00ac9f64)
  - `FALL_THROUGH` [`00ac9e38`](#insn-00ac9e38) → [`00ac9e3c`](#insn-00ac9e3c)
- ブロック [`00ac9e3c`](#insn-00ac9e3c) 範囲 `[['00ac9e3c', '00ac9e6f']]`
  - `CONDITIONAL_JUMP` [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9ed4`](#insn-00ac9ed4)
  - `FALL_THROUGH` [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9e70`](#insn-00ac9e70)
- ブロック [`00ac9e70`](#insn-00ac9e70) 範囲 `[['00ac9e70', '00ac9e77']]`
  - `CONDITIONAL_JUMP` [`00ac9e74`](#insn-00ac9e74) → [`00ac9f6c`](#insn-00ac9f6c)
  - `FALL_THROUGH` [`00ac9e74`](#insn-00ac9e74) → [`00ac9e78`](#insn-00ac9e78)
- ブロック [`00ac9e78`](#insn-00ac9e78) 範囲 `[['00ac9e78', '00ac9e8f']]`
  - `UNCONDITIONAL_JUMP` [`00ac9e8c`](#insn-00ac9e8c) → [`00ac9ed8`](#insn-00ac9ed8)
- ブロック [`00ac9e90`](#insn-00ac9e90) 範囲 `[['00ac9e90', '00ac9e93']]`
  - `CONDITIONAL_JUMP` [`00ac9e90`](#insn-00ac9e90) → [`00ac9ecc`](#insn-00ac9ecc)
  - `FALL_THROUGH` [`00ac9e90`](#insn-00ac9e90) → [`00ac9e94`](#insn-00ac9e94)
- ブロック [`00ac9e94`](#insn-00ac9e94) 範囲 `[['00ac9e94', '00ac9ecb']]`
  - `FALL_THROUGH` [`00ac9ec8`](#insn-00ac9ec8) → [`00ac9ecc`](#insn-00ac9ecc)
- ブロック [`00ac9ecc`](#insn-00ac9ecc) 範囲 `[['00ac9ecc', '00ac9ed3']]`
  - `UNCONDITIONAL_JUMP` [`00ac9ed0`](#insn-00ac9ed0) → [`00ac9f4c`](#insn-00ac9f4c)
- ブロック [`00ac9ed4`](#insn-00ac9ed4) 範囲 `[['00ac9ed4', '00ac9ed7']]`
  - `FALL_THROUGH` [`00ac9ed4`](#insn-00ac9ed4) → [`00ac9ed8`](#insn-00ac9ed8)
- ブロック [`00ac9ed8`](#insn-00ac9ed8) 範囲 `[['00ac9ed8', '00ac9f2f']]`
  - `CONDITIONAL_JUMP` [`00ac9f2c`](#insn-00ac9f2c) → [`00ac9f4c`](#insn-00ac9f4c)
  - `FALL_THROUGH` [`00ac9f2c`](#insn-00ac9f2c) → [`00ac9f30`](#insn-00ac9f30)
- ブロック [`00ac9f30`](#insn-00ac9f30) 範囲 `[['00ac9f30', '00ac9f4b']]`
- ブロック [`00ac9f4c`](#insn-00ac9f4c) 範囲 `[['00ac9f4c', '00ac9f63']]`
- ブロック [`00ac9f64`](#insn-00ac9f64) 範囲 `[['00ac9f64', '00ac9f6b']]`
  - `FALL_THROUGH` [`00ac9f68`](#insn-00ac9f68) → [`00ac9f6c`](#insn-00ac9f6c)
- ブロック [`00ac9f6c`](#insn-00ac9f6c) 範囲 `[['00ac9f6c', '00ac9f6f']]`

## 命令位置別の参照

- [`00ac9ddc`](#insn-00ac9ddc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9de0`](#insn-00ac9de0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9de4`](#insn-00ac9de4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9de8`](#insn-00ac9de8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9dec`](#insn-00ac9dec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e14`](#insn-00ac9e14) → [`00ac9e90`](#insn-00ac9e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e38`](#insn-00ac9e38) → [`00ac9f64`](#insn-00ac9f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e6c`](#insn-00ac9e6c) → [`00ac9ed4`](#insn-00ac9ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e74`](#insn-00ac9e74) → [`00ac9f6c`](#insn-00ac9f6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e84`](#insn-00ac9e84) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e8c`](#insn-00ac9e8c) → [`00ac9ed8`](#insn-00ac9ed8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9e90`](#insn-00ac9e90) → [`00ac9ecc`](#insn-00ac9ecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ec4`](#insn-00ac9ec4) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ed0`](#insn-00ac9ed0) → [`00ac9f4c`](#insn-00ac9f4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f08`](#insn-00ac9f08) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f20`](#insn-00ac9f20) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f2c`](#insn-00ac9f2c) → [`00ac9f4c`](#insn-00ac9f4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f34`](#insn-00ac9f34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f38`](#insn-00ac9f38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f3c`](#insn-00ac9f3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f40`](#insn-00ac9f40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f44`](#insn-00ac9f44) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f48`](#insn-00ac9f48) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f4c`](#insn-00ac9f4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f50`](#insn-00ac9f50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f54`](#insn-00ac9f54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f58`](#insn-00ac9f58) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f5c`](#insn-00ac9f5c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f68`](#insn-00ac9f68) → [`00ac9f70`](00ac9f70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9f70` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f6c`](#insn-00ac9f6c) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac9ddc`](#insn-00ac9ddc)

~~~json
{
  "source": "00ac9ddc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9de0`](#insn-00ac9de0)

~~~json
{
  "source": "00ac9de0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9de4`](#insn-00ac9de4)

~~~json
{
  "source": "00ac9de4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9de8`](#insn-00ac9de8)

~~~json
{
  "source": "00ac9de8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9dec`](#insn-00ac9dec)

~~~json
{
  "source": "00ac9dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e14`](#insn-00ac9e14)

~~~json
{
  "source": "00ac9e14",
  "target": "00ac9e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e38`](#insn-00ac9e38)

~~~json
{
  "source": "00ac9e38",
  "target": "00ac9f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e6c`](#insn-00ac9e6c)

~~~json
{
  "source": "00ac9e6c",
  "target": "00ac9ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e74`](#insn-00ac9e74)

~~~json
{
  "source": "00ac9e74",
  "target": "00ac9f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e84`](#insn-00ac9e84)

~~~json
{
  "source": "00ac9e84",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9e8c`](#insn-00ac9e8c)

~~~json
{
  "source": "00ac9e8c",
  "target": "00ac9ed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9e90`](#insn-00ac9e90)

~~~json
{
  "source": "00ac9e90",
  "target": "00ac9ecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ec4`](#insn-00ac9ec4)

~~~json
{
  "source": "00ac9ec4",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9ed0`](#insn-00ac9ed0)

~~~json
{
  "source": "00ac9ed0",
  "target": "00ac9f4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f08`](#insn-00ac9f08)

~~~json
{
  "source": "00ac9f08",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9f20`](#insn-00ac9f20)

~~~json
{
  "source": "00ac9f20",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9f2c`](#insn-00ac9f2c)

~~~json
{
  "source": "00ac9f2c",
  "target": "00ac9f4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f34`](#insn-00ac9f34)

~~~json
{
  "source": "00ac9f34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f38`](#insn-00ac9f38)

~~~json
{
  "source": "00ac9f38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f3c`](#insn-00ac9f3c)

~~~json
{
  "source": "00ac9f3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f40`](#insn-00ac9f40)

~~~json
{
  "source": "00ac9f40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f44`](#insn-00ac9f44)

~~~json
{
  "source": "00ac9f44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f48`](#insn-00ac9f48)

~~~json
{
  "source": "00ac9f48",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9f4c`](#insn-00ac9f4c)

~~~json
{
  "source": "00ac9f4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f50`](#insn-00ac9f50)

~~~json
{
  "source": "00ac9f50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f54`](#insn-00ac9f54)

~~~json
{
  "source": "00ac9f54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f58`](#insn-00ac9f58)

~~~json
{
  "source": "00ac9f58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f5c`](#insn-00ac9f5c)

~~~json
{
  "source": "00ac9f5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f68`](#insn-00ac9f68)

~~~json
{
  "source": "00ac9f68",
  "target": "00ac9f70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9f6c`](#insn-00ac9f6c)

~~~json
{
  "source": "00ac9f6c",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
