# 00ac9ebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ac9f84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-a10a6e6c7799a2a84325173a0f9d15d4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9ebc",
  "name": "FUN_00ac9ebc",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fcf4cb2dea5f9371cc7db1c7b46c62613952176d55ddb653fb7110720a683a7",
  "source_text_sha256": "3fcf4cb2dea5f9371cc7db1c7b46c62613952176d55ddb653fb7110720a683a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9ebc",
        "00aca04b"
      ]
    ],
    "bytes_sha256": "44ede31714ff3e794cfcea7f7fbe23405b71dfb8ba6a36625f71a8e84a99f7a0",
    "instruction_count": 100,
    "instruction_bytes": 400,
    "body_bytes": 400,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ab3338](../00ab3/00ab3338.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aca04c](../00aca/00aca04c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb140](../00bdb/00bdb140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1618 bytes

~~~c

void FUN_00ac9ebc(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  void *__src;
  size_t sVar4;
  void *pvVar5;
  size_t __n;
  
  pvVar5 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar5 >> 4) * -0x1111111111111111) < param_2) {
    __src = (void *)*param_1;
    sVar4 = (long)pvVar5 - (long)__src;
    uVar1 = ((long)sVar4 >> 4) * -0x1111111111111111 + param_2;
    if (0x111111111111111 < uVar1) {
      FUN_00aca04c(param_1);
LAB_00aca048:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar2 = param_1[2] - (long)__src >> 4;
    uVar3 = lVar2 * -0x2222222222222222;
    if (uVar3 < uVar1 || uVar3 - uVar1 == 0) {
      uVar3 = uVar1;
    }
    if (0x88888888888887 < (ulong)(lVar2 * -0x1111111111111111)) {
      uVar3 = 0x111111111111111;
    }
    if (uVar3 == 0) {
      lVar2 = 0;
    }
    else {
      if (0x111111111111111 < uVar3) goto LAB_00aca048;
      lVar2 = _Znwm(uVar3 * 0xf0);
    }
    pvVar5 = (void *)(lVar2 + ((long)sVar4 >> 4) * 0x10);
    __n = ((param_2 * 0xf0 - 0xf0) / 0xf0) * 0xf0 + 0xf0;
    memset(pvVar5,0,__n);
    memcpy((void *)((long)pvVar5 - sVar4),__src,sVar4);
    *param_1 = (void *)((long)pvVar5 - sVar4);
    param_1[1] = (long)pvVar5 + __n;
    param_1[2] = lVar2 + uVar3 * 0xf0;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar4 = ((param_2 * 0xf0 - 0xf0) / 0xf0) * 0xf0 + 0xf0;
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
<a id="insn-00ac9ebc"></a> `00ac9ebc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ac9ec0"></a> `00ac9ec0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9ec4"></a> `00ac9ec4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9ec8"></a> `00ac9ec8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac9ecc"></a> `00ac9ecc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac9ed0"></a> `00ac9ed0` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9ed4"></a> `00ac9ed4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac9ed8"></a> `00ac9ed8` | `09 01 15 cb` | sub x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00ac9edc"></a> `00ac9edc` | `2a fd 44 93` | asr x10,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9ee0"></a> `00ac9ee0` | `e9 eb 03 b2` | orr x9,xzr,#-0x1111111111111112 | `FALL_THROUGH`
<a id="insn-00ac9ee4"></a> `00ac9ee4` | `e9 dd 9d f2` | movk x9,#0xeeef | `FALL_THROUGH`
<a id="insn-00ac9ee8"></a> `00ac9ee8` | `4a 7d 09 9b` | mul x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9eec"></a> `00ac9eec` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00ac9ef0"></a> `00ac9ef0` | `e2 03 00 54` | b.cs 0x00ac9f6c | `CONDITIONAL_JUMP`
<a id="insn-00ac9ef4"></a> `00ac9ef4` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00ac9ef8"></a> `00ac9ef8` | `b5 02 14 cb` | sub x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9efc"></a> `00ac9efc` | `aa fe 44 93` | asr x10,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9f00"></a> `00ac9f00` | `56 7d 09 9b` | mul x22,x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9f04"></a> `00ac9f04` | `e9 e3 00 b2` | orr x9,xzr,#0x1111111111111111 | `FALL_THROUGH`
<a id="insn-00ac9f08"></a> `00ac9f08` | `29 22 e0 f2` | movk x9,#0x111, LSL #48 | `FALL_THROUGH`
<a id="insn-00ac9f0c"></a> `00ac9f0c` | `ca 02 01 8b` | add x10,x22,x1 | `FALL_THROUGH`
<a id="insn-00ac9f10"></a> `00ac9f10` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00ac9f14"></a> `00ac9f14` | `68 09 00 54` | b.hi 0x00aca040 | `CONDITIONAL_JUMP`
<a id="insn-00ac9f18"></a> `00ac9f18` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00ac9f1c"></a> `00ac9f1c` | `eb eb 03 b2` | orr x11,xzr,#-0x1111111111111112 | `FALL_THROUGH`
<a id="insn-00ac9f20"></a> `00ac9f20` | `ec e3 01 b2` | orr x12,xzr,#-0x7777777777777778 | `FALL_THROUGH`
<a id="insn-00ac9f24"></a> `00ac9f24` | `08 fd 44 93` | asr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ac9f28"></a> `00ac9f28` | `eb dd 9d f2` | movk x11,#0xeeef | `FALL_THROUGH`
<a id="insn-00ac9f2c"></a> `00ac9f2c` | `0c 11 e0 f2` | movk x12,#0x88, LSL #48 | `FALL_THROUGH`
<a id="insn-00ac9f30"></a> `00ac9f30` | `08 7d 0b 9b` | mul x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00ac9f34"></a> `00ac9f34` | `0b f9 7f d3` | lsl x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9f38"></a> `00ac9f38` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00ac9f3c"></a> `00ac9f3c` | `6a 81 8a 9a` | csel x10,x11,x10,hi | `FALL_THROUGH`
<a id="insn-00ac9f40"></a> `00ac9f40` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00ac9f44"></a> `00ac9f44` | `57 31 89 9a` | csel x23,x10,x9,cc | `FALL_THROUGH`
<a id="insn-00ac9f48"></a> `00ac9f48` | `57 03 00 b4` | cbz x23,0x00ac9fb0 | `CONDITIONAL_JUMP`
<a id="insn-00ac9f4c"></a> `00ac9f4c` | `ff 02 09 eb` | cmp x23,x9 | `FALL_THROUGH`
<a id="insn-00ac9f50"></a> `00ac9f50` | `c8 07 00 54` | b.hi 0x00aca048 | `CONDITIONAL_JUMP`
<a id="insn-00ac9f54"></a> `00ac9f54` | `e8 de 78 d3` | lsl x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00ac9f58"></a> `00ac9f58` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00ac9f5c"></a> `00ac9f5c` | `00 11 17 cb` | sub x0,x8,x23, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00ac9f60"></a> `00ac9f60` | `f8 43 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9f64"></a> `00ac9f64` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00ac9f68"></a> `00ac9f68` | `13 00 00 14` | b 0x00ac9fb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9f6c"></a> `00ac9f6c` | `e1 01 00 b4` | cbz x1,0x00ac9fa8 | `CONDITIONAL_JUMP`
<a id="insn-00ac9f70"></a> `00ac9f70` | `08 1e 80 52` | mov w8,#0xf0 | `FALL_THROUGH`
<a id="insn-00ac9f74"></a> `00ac9f74` | `e9 1d 80 92` | mov x9,#-0xf0 | `FALL_THROUGH`
<a id="insn-00ac9f78"></a> `00ac9f78` | `ea e3 01 b2` | orr x10,xzr,#-0x7777777777777778 | `FALL_THROUGH`
<a id="insn-00ac9f7c"></a> `00ac9f7c` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9f80"></a> `00ac9f80` | `2a 11 91 f2` | movk x10,#0x8889 | `FALL_THROUGH`
<a id="insn-00ac9f84"></a> `00ac9f84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac9f88"></a> `00ac9f88` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9f8c"></a> `00ac9f8c` | `29 7d ca 9b` | umulh x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ac9f90"></a> `00ac9f90` | `0a 1e 80 d2` | mov x10,#0xf0 | `FALL_THROUGH`
<a id="insn-00ac9f94"></a> `00ac9f94` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ac9f98"></a> `00ac9f98` | `34 29 08 9b` | madd x20,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00ac9f9c"></a> `00ac9f9c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ac9fa0"></a> `00ac9fa0` | `68 44 04 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9fa4"></a> `00ac9fa4` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00ac9fa8"></a> `00ac9fa8` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ac9fac"></a> `00ac9fac` | `20 00 00 14` | b 0x00aca02c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9fb0"></a> `00ac9fb0` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00ac9fb4"></a> `00ac9fb4` | `08 1e 80 52` | mov w8,#0xf0 | `FALL_THROUGH`
<a id="insn-00ac9fb8"></a> `00ac9fb8` | `e9 1d 80 92` | mov x9,#-0xf0 | `FALL_THROUGH`
<a id="insn-00ac9fbc"></a> `00ac9fbc` | `ea e3 01 b2` | orr x10,xzr,#-0x7777777777777778 | `FALL_THROUGH`
<a id="insn-00ac9fc0"></a> `00ac9fc0` | `29 24 08 9b` | madd x9,x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9fc4"></a> `00ac9fc4` | `2a 11 91 f2` | movk x10,#0x8889 | `FALL_THROUGH`
<a id="insn-00ac9fc8"></a> `00ac9fc8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ac9fcc"></a> `00ac9fcc` | `d6 02 08 9b` | madd x22,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00ac9fd0"></a> `00ac9fd0` | `f8 02 08 9b` | madd x24,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-00ac9fd4"></a> `00ac9fd4` | `29 7d ca 9b` | umulh x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ac9fd8"></a> `00ac9fd8` | `0a 1e 80 d2` | mov x10,#0xf0 | `FALL_THROUGH`
<a id="insn-00ac9fdc"></a> `00ac9fdc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9fe0"></a> `00ac9fe0` | `29 fd 47 d3` | lsr x9,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ac9fe4"></a> `00ac9fe4` | `37 29 08 9b` | madd x23,x9,x8,x10 | `FALL_THROUGH`
<a id="insn-00ac9fe8"></a> `00ac9fe8` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00ac9fec"></a> `00ac9fec` | `55 44 04 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9ff0"></a> `00ac9ff0` | `d7 02 17 8b` | add x23,x22,x23 | `FALL_THROUGH`
<a id="insn-00ac9ff4"></a> `00ac9ff4` | `d6 02 15 cb` | sub x22,x22,x21 | `FALL_THROUGH`
<a id="insn-00ac9ff8"></a> `00ac9ff8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ac9ffc"></a> `00ac9ffc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aca000"></a> `00aca000` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aca004"></a> `00aca004` | `2b 44 04 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aca008"></a> `00aca008` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00aca00c"></a> `00aca00c` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aca010"></a> `00aca010` | `f4 00 00 b4` | cbz x20,0x00aca02c | `CONDITIONAL_JUMP`
<a id="insn-00aca014"></a> `00aca014` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aca018"></a> `00aca018` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca01c"></a> `00aca01c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca020"></a> `00aca020` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca024"></a> `00aca024` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aca028"></a> `00aca028` | `ce 43 04 14` | b 0x00bdaf60 | `CALL_TERMINATOR`
<a id="insn-00aca02c"></a> `00aca02c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca030"></a> `00aca030` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca034"></a> `00aca034` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca038"></a> `00aca038` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aca03c"></a> `00aca03c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aca040"></a> `00aca040` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca044"></a> `00aca044` | `02 00 00 94` | bl 0x00aca04c | `UNCONDITIONAL_CALL`
<a id="insn-00aca048"></a> `00aca048` | `ce 50 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9ebc`](#insn-00ac9ebc) 範囲 `[['00ac9ebc', '00ac9ef3']]`
  - `CONDITIONAL_JUMP` [`00ac9ef0`](#insn-00ac9ef0) → [`00ac9f6c`](#insn-00ac9f6c)
  - `FALL_THROUGH` [`00ac9ef0`](#insn-00ac9ef0) → [`00ac9ef4`](#insn-00ac9ef4)
- ブロック [`00ac9ef4`](#insn-00ac9ef4) 範囲 `[['00ac9ef4', '00ac9f17']]`
  - `CONDITIONAL_JUMP` [`00ac9f14`](#insn-00ac9f14) → [`00aca040`](#insn-00aca040)
  - `FALL_THROUGH` [`00ac9f14`](#insn-00ac9f14) → [`00ac9f18`](#insn-00ac9f18)
- ブロック [`00ac9f18`](#insn-00ac9f18) 範囲 `[['00ac9f18', '00ac9f4b']]`
  - `CONDITIONAL_JUMP` [`00ac9f48`](#insn-00ac9f48) → [`00ac9fb0`](#insn-00ac9fb0)
  - `FALL_THROUGH` [`00ac9f48`](#insn-00ac9f48) → [`00ac9f4c`](#insn-00ac9f4c)
- ブロック [`00ac9f4c`](#insn-00ac9f4c) 範囲 `[['00ac9f4c', '00ac9f53']]`
  - `CONDITIONAL_JUMP` [`00ac9f50`](#insn-00ac9f50) → [`00aca048`](#insn-00aca048)
  - `FALL_THROUGH` [`00ac9f50`](#insn-00ac9f50) → [`00ac9f54`](#insn-00ac9f54)
- ブロック [`00ac9f54`](#insn-00ac9f54) 範囲 `[['00ac9f54', '00ac9f6b']]`
  - `UNCONDITIONAL_JUMP` [`00ac9f68`](#insn-00ac9f68) → [`00ac9fb4`](#insn-00ac9fb4)
- ブロック [`00ac9f6c`](#insn-00ac9f6c) 範囲 `[['00ac9f6c', '00ac9f6f']]`
  - `CONDITIONAL_JUMP` [`00ac9f6c`](#insn-00ac9f6c) → [`00ac9fa8`](#insn-00ac9fa8)
  - `FALL_THROUGH` [`00ac9f6c`](#insn-00ac9f6c) → [`00ac9f70`](#insn-00ac9f70)
- ブロック [`00ac9f70`](#insn-00ac9f70) 範囲 `[['00ac9f70', '00ac9fa7']]`
  - `FALL_THROUGH` [`00ac9fa4`](#insn-00ac9fa4) → [`00ac9fa8`](#insn-00ac9fa8)
- ブロック [`00ac9fa8`](#insn-00ac9fa8) 範囲 `[['00ac9fa8', '00ac9faf']]`
  - `UNCONDITIONAL_JUMP` [`00ac9fac`](#insn-00ac9fac) → [`00aca02c`](#insn-00aca02c)
- ブロック [`00ac9fb0`](#insn-00ac9fb0) 範囲 `[['00ac9fb0', '00ac9fb3']]`
  - `FALL_THROUGH` [`00ac9fb0`](#insn-00ac9fb0) → [`00ac9fb4`](#insn-00ac9fb4)
- ブロック [`00ac9fb4`](#insn-00ac9fb4) 範囲 `[['00ac9fb4', '00aca013']]`
  - `CONDITIONAL_JUMP` [`00aca010`](#insn-00aca010) → [`00aca02c`](#insn-00aca02c)
  - `FALL_THROUGH` [`00aca010`](#insn-00aca010) → [`00aca014`](#insn-00aca014)
- ブロック [`00aca014`](#insn-00aca014) 範囲 `[['00aca014', '00aca02b']]`
- ブロック [`00aca02c`](#insn-00aca02c) 範囲 `[['00aca02c', '00aca03f']]`
- ブロック [`00aca040`](#insn-00aca040) 範囲 `[['00aca040', '00aca047']]`
  - `FALL_THROUGH` [`00aca044`](#insn-00aca044) → [`00aca048`](#insn-00aca048)
- ブロック [`00aca048`](#insn-00aca048) 範囲 `[['00aca048', '00aca04b']]`

## 命令位置別の参照

- [`00ac9ebc`](#insn-00ac9ebc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ec0`](#insn-00ac9ec0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ec4`](#insn-00ac9ec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ec8`](#insn-00ac9ec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ef0`](#insn-00ac9ef0) → [`00ac9f6c`](#insn-00ac9f6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f14`](#insn-00ac9f14) → [`00aca040`](#insn-00aca040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f48`](#insn-00ac9f48) → [`00ac9fb0`](#insn-00ac9fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f50`](#insn-00ac9f50) → [`00aca048`](#insn-00aca048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f60`](#insn-00ac9f60) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f68`](#insn-00ac9f68) → [`00ac9fb4`](#insn-00ac9fb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9f6c`](#insn-00ac9f6c) → [`00ac9fa8`](#insn-00ac9fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9fa0`](#insn-00ac9fa0) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00ac9fac`](#insn-00ac9fac) → [`00aca02c`](#insn-00aca02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9fec`](#insn-00ac9fec) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00aca004`](#insn-00aca004) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00aca010`](#insn-00aca010) → [`00aca02c`](#insn-00aca02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca018`](#insn-00aca018) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca01c`](#insn-00aca01c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca020`](#insn-00aca020) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca024`](#insn-00aca024) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca028`](#insn-00aca028) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aca02c`](#insn-00aca02c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca030`](#insn-00aca030) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca034`](#insn-00aca034) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca038`](#insn-00aca038) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca044`](#insn-00aca044) → [`00aca04c`](../00aca/00aca04c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aca04c` · 推定シンボル `None` · 推定型 `None`
- [`00aca048`](#insn-00aca048) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac9ebc`](#insn-00ac9ebc)

~~~json
{
  "source": "00ac9ebc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ec0`](#insn-00ac9ec0)

~~~json
{
  "source": "00ac9ec0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ec4`](#insn-00ac9ec4)

~~~json
{
  "source": "00ac9ec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ec8`](#insn-00ac9ec8)

~~~json
{
  "source": "00ac9ec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ef0`](#insn-00ac9ef0)

~~~json
{
  "source": "00ac9ef0",
  "target": "00ac9f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f14`](#insn-00ac9f14)

~~~json
{
  "source": "00ac9f14",
  "target": "00aca040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f48`](#insn-00ac9f48)

~~~json
{
  "source": "00ac9f48",
  "target": "00ac9fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f50`](#insn-00ac9f50)

~~~json
{
  "source": "00ac9f50",
  "target": "00aca048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f60`](#insn-00ac9f60)

~~~json
{
  "source": "00ac9f60",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9f68`](#insn-00ac9f68)

~~~json
{
  "source": "00ac9f68",
  "target": "00ac9fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9f6c`](#insn-00ac9f6c)

~~~json
{
  "source": "00ac9f6c",
  "target": "00ac9fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9fa0`](#insn-00ac9fa0)

~~~json
{
  "source": "00ac9fa0",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9fac`](#insn-00ac9fac)

~~~json
{
  "source": "00ac9fac",
  "target": "00aca02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9fec`](#insn-00ac9fec)

~~~json
{
  "source": "00ac9fec",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca004`](#insn-00aca004)

~~~json
{
  "source": "00aca004",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca010`](#insn-00aca010)

~~~json
{
  "source": "00aca010",
  "target": "00aca02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca018`](#insn-00aca018)

~~~json
{
  "source": "00aca018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca01c`](#insn-00aca01c)

~~~json
{
  "source": "00aca01c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca020`](#insn-00aca020)

~~~json
{
  "source": "00aca020",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca024`](#insn-00aca024)

~~~json
{
  "source": "00aca024",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca028`](#insn-00aca028)

~~~json
{
  "source": "00aca028",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca02c`](#insn-00aca02c)

~~~json
{
  "source": "00aca02c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca030`](#insn-00aca030)

~~~json
{
  "source": "00aca030",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca034`](#insn-00aca034)

~~~json
{
  "source": "00aca034",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca038`](#insn-00aca038)

~~~json
{
  "source": "00aca038",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca044`](#insn-00aca044)

~~~json
{
  "source": "00aca044",
  "target": "00aca04c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca048`](#insn-00aca048)

~~~json
{
  "source": "00aca048",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
