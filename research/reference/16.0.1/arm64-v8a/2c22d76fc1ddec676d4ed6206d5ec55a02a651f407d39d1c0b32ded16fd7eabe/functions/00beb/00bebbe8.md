# 00bebbe8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00beb7c0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0013.md#compare-cc77b624dbbe958f35a4f29d5a7fb280)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bebc84`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebc84.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0014.md#compare-32aab5204d03a2a31f683578066c4bd6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebbe8",
  "name": "FUN_00bebbe8",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53",
  "source_text_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebbe8",
        "00bebd0f"
      ]
    ],
    "bytes_sha256": "54649e004bb31c060d4ebf17684a63401074f44dafc9fe8def557da592222551",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be4d98](../00be4/00be4d98.md)
- [00beb948](../00beb/00beb948.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1473 bytes

~~~c

void FUN_00bebbe8(int *param_1,int *param_2,int *param_3,int *param_4,int *param_5)

{
  int iVar1;
  int iVar2;
  int iVar3;
  
  iVar1 = *param_2;
  iVar2 = *param_1;
  iVar3 = *param_3;
  if (iVar1 < iVar2) {
    if (iVar3 < iVar1) {
      *param_1 = iVar3;
    }
    else {
      *param_1 = iVar1;
      *param_2 = iVar2;
      iVar3 = *param_3;
      if (iVar2 <= iVar3) goto LAB_00bebc68;
      *param_2 = iVar3;
    }
    *param_3 = iVar2;
    iVar3 = iVar2;
  }
  else if (iVar3 < iVar1) {
    *param_2 = iVar3;
    *param_3 = iVar1;
    iVar2 = *param_1;
    iVar3 = iVar1;
    if (*param_2 < iVar2) {
      *param_1 = *param_2;
      *param_2 = iVar2;
      iVar3 = *param_3;
    }
  }
LAB_00bebc68:
  if (*param_4 < iVar3) {
    *param_3 = *param_4;
    *param_4 = iVar3;
    iVar1 = *param_2;
    if (*param_3 < iVar1) {
      *param_2 = *param_3;
      *param_3 = iVar1;
      iVar1 = *param_1;
      if (*param_2 < iVar1) {
        *param_1 = *param_2;
        *param_2 = iVar1;
      }
    }
  }
  iVar1 = *param_4;
  if (*param_5 < iVar1) {
    *param_4 = *param_5;
    *param_5 = iVar1;
    iVar1 = *param_3;
    if (*param_4 < iVar1) {
      *param_3 = *param_4;
      *param_4 = iVar1;
      iVar1 = *param_2;
      if (*param_3 < iVar1) {
        *param_2 = *param_3;
        *param_3 = iVar1;
        iVar1 = *param_1;
        if (*param_2 < iVar1) {
          *param_1 = *param_2;
          *param_2 = iVar1;
        }
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bebbe8"></a> `00bebbe8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bebbec"></a> `00bebbec` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebbf0"></a> `00bebbf0` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebbf4"></a> `00bebbf4` | `4a 00 40 b9` | ldr w10,[x2] | `FALL_THROUGH`
<a id="insn-00bebbf8"></a> `00bebbf8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebbfc"></a> `00bebbfc` | `aa 00 00 54` | b.ge 0x00bebc10 | `CONDITIONAL_JUMP`
<a id="insn-00bebc00"></a> `00bebc00` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bebc04"></a> `00bebc04` | `ea 01 00 54` | b.ge 0x00bebc40 | `CONDITIONAL_JUMP`
<a id="insn-00bebc08"></a> `00bebc08` | `0a 00 00 b9` | str w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebc0c"></a> `00bebc0c` | `13 00 00 14` | b 0x00bebc58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc10"></a> `00bebc10` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bebc14"></a> `00bebc14` | `8a 02 00 54` | b.ge 0x00bebc64 | `CONDITIONAL_JUMP`
<a id="insn-00bebc18"></a> `00bebc18` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bebc1c"></a> `00bebc1c` | `48 00 00 b9` | str w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebc20"></a> `00bebc20` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebc24"></a> `00bebc24` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebc28"></a> `00bebc28` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bebc2c"></a> `00bebc2c` | `ea 01 00 54` | b.ge 0x00bebc68 | `CONDITIONAL_JUMP`
<a id="insn-00bebc30"></a> `00bebc30` | `09 00 00 b9` | str w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebc34"></a> `00bebc34` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bebc38"></a> `00bebc38` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebc3c"></a> `00bebc3c` | `0b 00 00 14` | b 0x00bebc68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc40"></a> `00bebc40` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebc44"></a> `00bebc44` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebc48"></a> `00bebc48` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebc4c"></a> `00bebc4c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebc50"></a> `00bebc50` | `ca 00 00 54` | b.ge 0x00bebc68 | `CONDITIONAL_JUMP`
<a id="insn-00bebc54"></a> `00bebc54` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebc58"></a> `00bebc58` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00bebc5c"></a> `00bebc5c` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebc60"></a> `00bebc60` | `02 00 00 14` | b 0x00bebc68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc64"></a> `00bebc64` | `e8 03 0a 2a` | mov w8,w10 | `FALL_THROUGH`
<a id="insn-00bebc68"></a> `00bebc68` | `69 00 40 b9` | ldr w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebc6c"></a> `00bebc6c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebc70"></a> `00bebc70` | `ea 01 00 54` | b.ge 0x00bebcac | `CONDITIONAL_JUMP`
<a id="insn-00bebc74"></a> `00bebc74` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebc78"></a> `00bebc78` | `68 00 00 b9` | str w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebc7c"></a> `00bebc7c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebc80"></a> `00bebc80` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebc84"></a> `00bebc84` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebc88"></a> `00bebc88` | `2a 01 00 54` | b.ge 0x00bebcac | `CONDITIONAL_JUMP`
<a id="insn-00bebc8c"></a> `00bebc8c` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebc90"></a> `00bebc90` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebc94"></a> `00bebc94` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebc98"></a> `00bebc98` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebc9c"></a> `00bebc9c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebca0"></a> `00bebca0` | `6a 00 00 54` | b.ge 0x00bebcac | `CONDITIONAL_JUMP`
<a id="insn-00bebca4"></a> `00bebca4` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebca8"></a> `00bebca8` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebcac"></a> `00bebcac` | `88 00 40 b9` | ldr w8,[x4] | `FALL_THROUGH`
<a id="insn-00bebcb0"></a> `00bebcb0` | `69 00 40 b9` | ldr w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebcb4"></a> `00bebcb4` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebcb8"></a> `00bebcb8` | `aa 02 00 54` | b.ge 0x00bebd0c | `CONDITIONAL_JUMP`
<a id="insn-00bebcbc"></a> `00bebcbc` | `68 00 00 b9` | str w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebcc0"></a> `00bebcc0` | `89 00 00 b9` | str w9,[x4] | `FALL_THROUGH`
<a id="insn-00bebcc4"></a> `00bebcc4` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebcc8"></a> `00bebcc8` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebccc"></a> `00bebccc` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebcd0"></a> `00bebcd0` | `ea 01 00 54` | b.ge 0x00bebd0c | `CONDITIONAL_JUMP`
<a id="insn-00bebcd4"></a> `00bebcd4` | `48 00 00 b9` | str w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebcd8"></a> `00bebcd8` | `69 00 00 b9` | str w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebcdc"></a> `00bebcdc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebce0"></a> `00bebce0` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebce4"></a> `00bebce4` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebce8"></a> `00bebce8` | `2a 01 00 54` | b.ge 0x00bebd0c | `CONDITIONAL_JUMP`
<a id="insn-00bebcec"></a> `00bebcec` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebcf0"></a> `00bebcf0` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebcf4"></a> `00bebcf4` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebcf8"></a> `00bebcf8` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebcfc"></a> `00bebcfc` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebd00"></a> `00bebd00` | `6a 00 00 54` | b.ge 0x00bebd0c | `CONDITIONAL_JUMP`
<a id="insn-00bebd04"></a> `00bebd04` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebd08"></a> `00bebd08` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebd0c"></a> `00bebd0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bebbe8`](#insn-00bebbe8) 範囲 `[['00bebbe8', '00bebbff']]`
  - `CONDITIONAL_JUMP` [`00bebbfc`](#insn-00bebbfc) → [`00bebc10`](#insn-00bebc10)
  - `FALL_THROUGH` [`00bebbfc`](#insn-00bebbfc) → [`00bebc00`](#insn-00bebc00)
- ブロック [`00bebc00`](#insn-00bebc00) 範囲 `[['00bebc00', '00bebc07']]`
  - `CONDITIONAL_JUMP` [`00bebc04`](#insn-00bebc04) → [`00bebc40`](#insn-00bebc40)
  - `FALL_THROUGH` [`00bebc04`](#insn-00bebc04) → [`00bebc08`](#insn-00bebc08)
- ブロック [`00bebc08`](#insn-00bebc08) 範囲 `[['00bebc08', '00bebc0f']]`
  - `UNCONDITIONAL_JUMP` [`00bebc0c`](#insn-00bebc0c) → [`00bebc58`](#insn-00bebc58)
- ブロック [`00bebc10`](#insn-00bebc10) 範囲 `[['00bebc10', '00bebc17']]`
  - `CONDITIONAL_JUMP` [`00bebc14`](#insn-00bebc14) → [`00bebc64`](#insn-00bebc64)
  - `FALL_THROUGH` [`00bebc14`](#insn-00bebc14) → [`00bebc18`](#insn-00bebc18)
- ブロック [`00bebc18`](#insn-00bebc18) 範囲 `[['00bebc18', '00bebc2f']]`
  - `CONDITIONAL_JUMP` [`00bebc2c`](#insn-00bebc2c) → [`00bebc68`](#insn-00bebc68)
  - `FALL_THROUGH` [`00bebc2c`](#insn-00bebc2c) → [`00bebc30`](#insn-00bebc30)
- ブロック [`00bebc30`](#insn-00bebc30) 範囲 `[['00bebc30', '00bebc3f']]`
  - `UNCONDITIONAL_JUMP` [`00bebc3c`](#insn-00bebc3c) → [`00bebc68`](#insn-00bebc68)
- ブロック [`00bebc40`](#insn-00bebc40) 範囲 `[['00bebc40', '00bebc53']]`
  - `CONDITIONAL_JUMP` [`00bebc50`](#insn-00bebc50) → [`00bebc68`](#insn-00bebc68)
  - `FALL_THROUGH` [`00bebc50`](#insn-00bebc50) → [`00bebc54`](#insn-00bebc54)
- ブロック [`00bebc54`](#insn-00bebc54) 範囲 `[['00bebc54', '00bebc57']]`
  - `FALL_THROUGH` [`00bebc54`](#insn-00bebc54) → [`00bebc58`](#insn-00bebc58)
- ブロック [`00bebc58`](#insn-00bebc58) 範囲 `[['00bebc58', '00bebc63']]`
  - `UNCONDITIONAL_JUMP` [`00bebc60`](#insn-00bebc60) → [`00bebc68`](#insn-00bebc68)
- ブロック [`00bebc64`](#insn-00bebc64) 範囲 `[['00bebc64', '00bebc67']]`
  - `FALL_THROUGH` [`00bebc64`](#insn-00bebc64) → [`00bebc68`](#insn-00bebc68)
- ブロック [`00bebc68`](#insn-00bebc68) 範囲 `[['00bebc68', '00bebc73']]`
  - `CONDITIONAL_JUMP` [`00bebc70`](#insn-00bebc70) → [`00bebcac`](#insn-00bebcac)
  - `FALL_THROUGH` [`00bebc70`](#insn-00bebc70) → [`00bebc74`](#insn-00bebc74)
- ブロック [`00bebc74`](#insn-00bebc74) 範囲 `[['00bebc74', '00bebc8b']]`
  - `CONDITIONAL_JUMP` [`00bebc88`](#insn-00bebc88) → [`00bebcac`](#insn-00bebcac)
  - `FALL_THROUGH` [`00bebc88`](#insn-00bebc88) → [`00bebc8c`](#insn-00bebc8c)
- ブロック [`00bebc8c`](#insn-00bebc8c) 範囲 `[['00bebc8c', '00bebca3']]`
  - `CONDITIONAL_JUMP` [`00bebca0`](#insn-00bebca0) → [`00bebcac`](#insn-00bebcac)
  - `FALL_THROUGH` [`00bebca0`](#insn-00bebca0) → [`00bebca4`](#insn-00bebca4)
- ブロック [`00bebca4`](#insn-00bebca4) 範囲 `[['00bebca4', '00bebcab']]`
  - `FALL_THROUGH` [`00bebca8`](#insn-00bebca8) → [`00bebcac`](#insn-00bebcac)
- ブロック [`00bebcac`](#insn-00bebcac) 範囲 `[['00bebcac', '00bebcbb']]`
  - `CONDITIONAL_JUMP` [`00bebcb8`](#insn-00bebcb8) → [`00bebd0c`](#insn-00bebd0c)
  - `FALL_THROUGH` [`00bebcb8`](#insn-00bebcb8) → [`00bebcbc`](#insn-00bebcbc)
- ブロック [`00bebcbc`](#insn-00bebcbc) 範囲 `[['00bebcbc', '00bebcd3']]`
  - `CONDITIONAL_JUMP` [`00bebcd0`](#insn-00bebcd0) → [`00bebd0c`](#insn-00bebd0c)
  - `FALL_THROUGH` [`00bebcd0`](#insn-00bebcd0) → [`00bebcd4`](#insn-00bebcd4)
- ブロック [`00bebcd4`](#insn-00bebcd4) 範囲 `[['00bebcd4', '00bebceb']]`
  - `CONDITIONAL_JUMP` [`00bebce8`](#insn-00bebce8) → [`00bebd0c`](#insn-00bebd0c)
  - `FALL_THROUGH` [`00bebce8`](#insn-00bebce8) → [`00bebcec`](#insn-00bebcec)
- ブロック [`00bebcec`](#insn-00bebcec) 範囲 `[['00bebcec', '00bebd03']]`
  - `CONDITIONAL_JUMP` [`00bebd00`](#insn-00bebd00) → [`00bebd0c`](#insn-00bebd0c)
  - `FALL_THROUGH` [`00bebd00`](#insn-00bebd00) → [`00bebd04`](#insn-00bebd04)
- ブロック [`00bebd04`](#insn-00bebd04) 範囲 `[['00bebd04', '00bebd0b']]`
  - `FALL_THROUGH` [`00bebd08`](#insn-00bebd08) → [`00bebd0c`](#insn-00bebd0c)
- ブロック [`00bebd0c`](#insn-00bebd0c) 範囲 `[['00bebd0c', '00bebd0f']]`

## 命令位置別の参照

- [`00bebbfc`](#insn-00bebbfc) → [`00bebc10`](#insn-00bebc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc04`](#insn-00bebc04) → [`00bebc40`](#insn-00bebc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc0c`](#insn-00bebc0c) → [`00bebc58`](#insn-00bebc58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc14`](#insn-00bebc14) → [`00bebc64`](#insn-00bebc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc2c`](#insn-00bebc2c) → [`00bebc68`](#insn-00bebc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc3c`](#insn-00bebc3c) → [`00bebc68`](#insn-00bebc68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc50`](#insn-00bebc50) → [`00bebc68`](#insn-00bebc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc60`](#insn-00bebc60) → [`00bebc68`](#insn-00bebc68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc70`](#insn-00bebc70) → [`00bebcac`](#insn-00bebcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc88`](#insn-00bebc88) → [`00bebcac`](#insn-00bebcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebca0`](#insn-00bebca0) → [`00bebcac`](#insn-00bebcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcb8`](#insn-00bebcb8) → [`00bebd0c`](#insn-00bebd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcd0`](#insn-00bebcd0) → [`00bebd0c`](#insn-00bebd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebce8`](#insn-00bebce8) → [`00bebd0c`](#insn-00bebd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd00`](#insn-00bebd00) → [`00bebd0c`](#insn-00bebd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bebbfc`](#insn-00bebbfc)

~~~json
{
  "source": "00bebbfc",
  "target": "00bebc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc04`](#insn-00bebc04)

~~~json
{
  "source": "00bebc04",
  "target": "00bebc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc0c`](#insn-00bebc0c)

~~~json
{
  "source": "00bebc0c",
  "target": "00bebc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc14`](#insn-00bebc14)

~~~json
{
  "source": "00bebc14",
  "target": "00bebc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc2c`](#insn-00bebc2c)

~~~json
{
  "source": "00bebc2c",
  "target": "00bebc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc3c`](#insn-00bebc3c)

~~~json
{
  "source": "00bebc3c",
  "target": "00bebc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc50`](#insn-00bebc50)

~~~json
{
  "source": "00bebc50",
  "target": "00bebc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc60`](#insn-00bebc60)

~~~json
{
  "source": "00bebc60",
  "target": "00bebc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc70`](#insn-00bebc70)

~~~json
{
  "source": "00bebc70",
  "target": "00bebcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc88`](#insn-00bebc88)

~~~json
{
  "source": "00bebc88",
  "target": "00bebcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebca0`](#insn-00bebca0)

~~~json
{
  "source": "00bebca0",
  "target": "00bebcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcb8`](#insn-00bebcb8)

~~~json
{
  "source": "00bebcb8",
  "target": "00bebd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcd0`](#insn-00bebcd0)

~~~json
{
  "source": "00bebcd0",
  "target": "00bebd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebce8`](#insn-00bebce8)

~~~json
{
  "source": "00bebce8",
  "target": "00bebd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd00`](#insn-00bebd00)

~~~json
{
  "source": "00bebd00",
  "target": "00bebd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
