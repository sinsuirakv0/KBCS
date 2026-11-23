# 00aa5edc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aa5edc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa5/00aa5edc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0007.md#compare-00bcd2db9f08e8d1c8bd1ba23a60f697)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aa5f20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa5/00aa5f20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-c71e9ccf207ef40035f42af4f913f3dd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa5edc",
  "name": "FUN_00aa5edc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d62d938fba8691c991752a432803b326d7419080ad78f685f8bbf028d5569f07",
  "source_text_sha256": "d62d938fba8691c991752a432803b326d7419080ad78f685f8bbf028d5569f07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa5edc",
        "00aa5f83"
      ]
    ],
    "bytes_sha256": "a179181af03a3e6b6c749fdd4fe183eb2a3db95bfb5f17887fd611ded215c56c",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009f1e64](../009f1/009f1e64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00a9f0e0](../00a9f/00a9f0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 560 bytes

~~~c

int FUN_00aa5edc(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_0081f580();
  uVar4 = FUN_005c2710(lVar3 + (long)param_1 * 0x1f0 + 0x2678);
  lVar3 = FUN_0081f580();
  if ((uVar4 & 1) == 0) {
    iVar2 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0xa520);
  }
  else {
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f054);
    iVar2 = FUN_00a9f0e0(param_1,param_2,param_3,0x43,2);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa5edc"></a> `00aa5edc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa5ee0"></a> `00aa5ee0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa5ee4"></a> `00aa5ee4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa5ee8"></a> `00aa5ee8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa5eec"></a> `00aa5eec` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa5ef0"></a> `00aa5ef0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa5ef4"></a> `00aa5ef4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa5ef8"></a> `00aa5ef8` | `a2 e5 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa5efc"></a> `00aa5efc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa5f00"></a> `00aa5f00` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa5f04"></a> `00aa5f04` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa5f08"></a> `00aa5f08` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa5f0c"></a> `00aa5f0c` | `01 72 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa5f10"></a> `00aa5f10` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa5f14"></a> `00aa5f14` | `9b e5 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa5f18"></a> `00aa5f18` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aa5f1c"></a> `00aa5f1c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa5f20"></a> `00aa5f20` | `f6 00 00 37` | tbnz w22,#0x0,0x00aa5f3c | `CONDITIONAL_JUMP`
<a id="insn-00aa5f24"></a> `00aa5f24` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa5f28"></a> `00aa5f28` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa5f2c"></a> `00aa5f2c` | `09 eb 93 52` | mov w9,#0x9f58 | `FALL_THROUGH`
<a id="insn-00aa5f30"></a> `00aa5f30` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa5f34"></a> `00aa5f34` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa5f38"></a> `00aa5f38` | `0f 00 00 14` | b 0x00aa5f74 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa5f3c"></a> `00aa5f3c` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aa5f40"></a> `00aa5f40` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa5f44"></a> `00aa5f44` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa5f48"></a> `00aa5f48` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aa5f4c"></a> `00aa5f4c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa5f50"></a> `00aa5f50` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00aa5f54"></a> `00aa5f54` | `63 08 80 52` | mov w3,#0x43 | `FALL_THROUGH`
<a id="insn-00aa5f58"></a> `00aa5f58` | `44 00 80 52` | mov w4,#0x2 | `FALL_THROUGH`
<a id="insn-00aa5f5c"></a> `00aa5f5c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa5f60"></a> `00aa5f60` | `89 0a 9e 52` | mov w9,#0xf054 | `FALL_THROUGH`
<a id="insn-00aa5f64"></a> `00aa5f64` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa5f68"></a> `00aa5f68` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa5f6c"></a> `00aa5f6c` | `5d e4 ff 97` | bl 0x00a9f0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa5f70"></a> `00aa5f70` | `00 00 16 0b` | add w0,w0,w22 | `FALL_THROUGH`
<a id="insn-00aa5f74"></a> `00aa5f74` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa5f78"></a> `00aa5f78` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa5f7c"></a> `00aa5f7c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa5f80"></a> `00aa5f80` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa5edc`](#insn-00aa5edc) 範囲 `[['00aa5edc', '00aa5f23']]`
  - `CONDITIONAL_JUMP` [`00aa5f20`](#insn-00aa5f20) → [`00aa5f3c`](#insn-00aa5f3c)
  - `FALL_THROUGH` [`00aa5f20`](#insn-00aa5f20) → [`00aa5f24`](#insn-00aa5f24)
- ブロック [`00aa5f24`](#insn-00aa5f24) 範囲 `[['00aa5f24', '00aa5f3b']]`
  - `UNCONDITIONAL_JUMP` [`00aa5f38`](#insn-00aa5f38) → [`00aa5f74`](#insn-00aa5f74)
- ブロック [`00aa5f3c`](#insn-00aa5f3c) 範囲 `[['00aa5f3c', '00aa5f73']]`
  - `FALL_THROUGH` [`00aa5f70`](#insn-00aa5f70) → [`00aa5f74`](#insn-00aa5f74)
- ブロック [`00aa5f74`](#insn-00aa5f74) 範囲 `[['00aa5f74', '00aa5f83']]`

## 命令位置別の参照

- [`00aa5edc`](#insn-00aa5edc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5ee0`](#insn-00aa5ee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5ee4`](#insn-00aa5ee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5ef8`](#insn-00aa5ef8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f0c`](#insn-00aa5f0c) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f14`](#insn-00aa5f14) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f20`](#insn-00aa5f20) → [`00aa5f3c`](#insn-00aa5f3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f34`](#insn-00aa5f34) → `00239f58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa5f38`](#insn-00aa5f38) → [`00aa5f74`](#insn-00aa5f74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f6c`](#insn-00aa5f6c) → [`00a9f0e0`](../00a9f/00a9f0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a9f0e0` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f74`](#insn-00aa5f74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f78`](#insn-00aa5f78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa5f7c`](#insn-00aa5f7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa5edc`](#insn-00aa5edc)

~~~json
{
  "source": "00aa5edc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5ee0`](#insn-00aa5ee0)

~~~json
{
  "source": "00aa5ee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5ee4`](#insn-00aa5ee4)

~~~json
{
  "source": "00aa5ee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5ef8`](#insn-00aa5ef8)

~~~json
{
  "source": "00aa5ef8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa5f0c`](#insn-00aa5f0c)

~~~json
{
  "source": "00aa5f0c",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa5f14`](#insn-00aa5f14)

~~~json
{
  "source": "00aa5f14",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa5f20`](#insn-00aa5f20)

~~~json
{
  "source": "00aa5f20",
  "target": "00aa5f3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5f34`](#insn-00aa5f34)

~~~json
{
  "source": "00aa5f34",
  "target": "00239f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42272,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "50c0b100000000000204000001000000000000000000000058c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa5f38`](#insn-00aa5f38)

~~~json
{
  "source": "00aa5f38",
  "target": "00aa5f74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5f6c`](#insn-00aa5f6c)

~~~json
{
  "source": "00aa5f6c",
  "target": "00a9f0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa5f74`](#insn-00aa5f74)

~~~json
{
  "source": "00aa5f74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5f78`](#insn-00aa5f78)

~~~json
{
  "source": "00aa5f78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa5f7c`](#insn-00aa5f7c)

~~~json
{
  "source": "00aa5f7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
