# 00a3becc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a3becc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3b/00a3becc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/reference_unresolved-0016.md#compare-735fbeb5f44cba9b8ad2beb5da258751)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a3bf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3bf10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-34805828be950c3c566d4fae2b1432f1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3becc",
  "name": "FUN_00a3becc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa34ca97ea40b64d5919b9afac0dcf6e3155840fadb654f5137ac211273d543",
  "source_text_sha256": "aaa34ca97ea40b64d5919b9afac0dcf6e3155840fadb654f5137ac211273d543",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3becc",
        "00a3bf37"
      ]
    ],
    "bytes_sha256": "35af55eeb6de77f0f9752f121510a00096c5b264fa88a459a563c5d96c464c27",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [0081f580](../0081f/0081f580.md)
- [008f9c04](../008f9/008f9c04.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 547 bytes

~~~c

void FUN_00a3becc(undefined8 param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar3 = FUN_0081f580();
    *(undefined1 *)(lVar3 + 0x20ff) = 0;
    lVar3 = FUN_0081f580();
    FUN_008f9c04(lVar3 + 0x472450,1);
    return;
  }
  if (iVar1 == 3) {
    uVar2 = FUN_00457e1c();
    uVar4 = 0xb;
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_00457e1c();
    uVar4 = 10;
  }
  FUN_00459efc(uVar2,uVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3becc"></a> `00a3becc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00a3bed0"></a> `00a3bed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3bed4"></a> `00a3bed4` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00a3bed8"></a> `00a3bed8` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00a3bedc"></a> `00a3bedc` | `80 01 00 54` | b.eq 0x00a3bf0c | `CONDITIONAL_JUMP`
<a id="insn-00a3bee0"></a> `00a3bee0` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a3bee4"></a> `00a3bee4` | `a0 00 00 54` | b.eq 0x00a3bef8 | `CONDITIONAL_JUMP`
<a id="insn-00a3bee8"></a> `00a3bee8` | `48 02 00 35` | cbnz w8,0x00a3bf30 | `CONDITIONAL_JUMP`
<a id="insn-00a3beec"></a> `00a3beec` | `cc 6f e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a3bef0"></a> `00a3bef0` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a3bef4"></a> `00a3bef4` | `03 00 00 14` | b 0x00a3bf00 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3bef8"></a> `00a3bef8` | `c9 6f e8 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00a3befc"></a> `00a3befc` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a3bf00"></a> `00a3bf00` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a3bf04"></a> `00a3bf04` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a3bf08"></a> `00a3bf08` | `fd 77 e8 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-00a3bf0c"></a> `00a3bf0c` | `9d 8d f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a3bf10"></a> `00a3bf10` | `e8 1f 84 52` | mov w8,#0x20ff | `FALL_THROUGH`
<a id="insn-00a3bf14"></a> `00a3bf14` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a3bf18"></a> `00a3bf18` | `9a 8d f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a3bf1c"></a> `00a3bf1c` | `08 c8 51 91` | add x8,x0,#0x472, LSL #12 | `FALL_THROUGH`
<a id="insn-00a3bf20"></a> `00a3bf20` | `00 41 11 91` | add x0,x8,#0x450 | `FALL_THROUGH`
<a id="insn-00a3bf24"></a> `00a3bf24` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a3bf28"></a> `00a3bf28` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a3bf2c"></a> `00a3bf2c` | `36 f7 fa 17` | b 0x008f9c04 | `CALL_TERMINATOR`
<a id="insn-00a3bf30"></a> `00a3bf30` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00a3bf34"></a> `00a3bf34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3becc`](#insn-00a3becc) 範囲 `[['00a3becc', '00a3bedf']]`
  - `CONDITIONAL_JUMP` [`00a3bedc`](#insn-00a3bedc) → [`00a3bf0c`](#insn-00a3bf0c)
  - `FALL_THROUGH` [`00a3bedc`](#insn-00a3bedc) → [`00a3bee0`](#insn-00a3bee0)
- ブロック [`00a3bee0`](#insn-00a3bee0) 範囲 `[['00a3bee0', '00a3bee7']]`
  - `CONDITIONAL_JUMP` [`00a3bee4`](#insn-00a3bee4) → [`00a3bef8`](#insn-00a3bef8)
  - `FALL_THROUGH` [`00a3bee4`](#insn-00a3bee4) → [`00a3bee8`](#insn-00a3bee8)
- ブロック [`00a3bee8`](#insn-00a3bee8) 範囲 `[['00a3bee8', '00a3beeb']]`
  - `CONDITIONAL_JUMP` [`00a3bee8`](#insn-00a3bee8) → [`00a3bf30`](#insn-00a3bf30)
  - `FALL_THROUGH` [`00a3bee8`](#insn-00a3bee8) → [`00a3beec`](#insn-00a3beec)
- ブロック [`00a3beec`](#insn-00a3beec) 範囲 `[['00a3beec', '00a3bef7']]`
  - `UNCONDITIONAL_JUMP` [`00a3bef4`](#insn-00a3bef4) → [`00a3bf00`](#insn-00a3bf00)
- ブロック [`00a3bef8`](#insn-00a3bef8) 範囲 `[['00a3bef8', '00a3beff']]`
  - `FALL_THROUGH` [`00a3befc`](#insn-00a3befc) → [`00a3bf00`](#insn-00a3bf00)
- ブロック [`00a3bf00`](#insn-00a3bf00) 範囲 `[['00a3bf00', '00a3bf0b']]`
- ブロック [`00a3bf0c`](#insn-00a3bf0c) 範囲 `[['00a3bf0c', '00a3bf2f']]`
- ブロック [`00a3bf30`](#insn-00a3bf30) 範囲 `[['00a3bf30', '00a3bf37']]`

## 命令位置別の参照

- [`00a3becc`](#insn-00a3becc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bedc`](#insn-00a3bedc) → [`00a3bf0c`](#insn-00a3bf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bee4`](#insn-00a3bee4) → [`00a3bef8`](#insn-00a3bef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bee8`](#insn-00a3bee8) → [`00a3bf30`](#insn-00a3bf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3beec`](#insn-00a3beec) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a3bef4`](#insn-00a3bef4) → [`00a3bf00`](#insn-00a3bf00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bef8`](#insn-00a3bef8) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf04`](#insn-00a3bf04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf08`](#insn-00a3bf08) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf0c`](#insn-00a3bf0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf18`](#insn-00a3bf18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf28`](#insn-00a3bf28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf2c`](#insn-00a3bf2c) → [`008f9c04`](../008f9/008f9c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008f9c04` · 推定シンボル `None` · 推定型 `None`
- [`00a3bf30`](#insn-00a3bf30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3becc`](#insn-00a3becc)

~~~json
{
  "source": "00a3becc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bedc`](#insn-00a3bedc)

~~~json
{
  "source": "00a3bedc",
  "target": "00a3bf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bee4`](#insn-00a3bee4)

~~~json
{
  "source": "00a3bee4",
  "target": "00a3bef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bee8`](#insn-00a3bee8)

~~~json
{
  "source": "00a3bee8",
  "target": "00a3bf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3beec`](#insn-00a3beec)

~~~json
{
  "source": "00a3beec",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bef4`](#insn-00a3bef4)

~~~json
{
  "source": "00a3bef4",
  "target": "00a3bf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bef8`](#insn-00a3bef8)

~~~json
{
  "source": "00a3bef8",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bf04`](#insn-00a3bf04)

~~~json
{
  "source": "00a3bf04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bf08`](#insn-00a3bf08)

~~~json
{
  "source": "00a3bf08",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bf0c`](#insn-00a3bf0c)

~~~json
{
  "source": "00a3bf0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bf18`](#insn-00a3bf18)

~~~json
{
  "source": "00a3bf18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bf28`](#insn-00a3bf28)

~~~json
{
  "source": "00a3bf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3bf2c`](#insn-00a3bf2c)

~~~json
{
  "source": "00a3bf2c",
  "target": "008f9c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3bf30`](#insn-00a3bf30)

~~~json
{
  "source": "00a3bf30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
