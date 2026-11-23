# 00aadadc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aada14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-1c0f3b3445aec4986efc55c0c2daeffc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aadb20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aad/00aadb20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-cfe42f6115c6427a2b6d8ea42d159e30)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadadc",
  "name": "FUN_00aadadc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a4ddff42a06a5d8b2d36b9360c6c90a6298c23fb12c3892e248e370d11004c3",
  "source_text_sha256": "7a4ddff42a06a5d8b2d36b9360c6c90a6298c23fb12c3892e248e370d11004c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadadc",
        "00aadb7b"
      ]
    ],
    "bytes_sha256": "4a23990e475207f1b54fadd6f5d35ada1250732e4bd8d8ed3470b4380449c3c1",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
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
- [00aab488](../00aab/00aab488.md)
- [00aabe04](../00aab/00aabe04.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 726 bytes

~~~c

void FUN_00aadadc(long param_1,undefined8 param_2,int *param_3)

{
  long lVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
  iVar2 = *param_3;
  if (iVar2 == 4) {
    lVar1 = *(long *)(param_1 + 8);
    uVar5 = *(undefined8 *)(param_1 + 0x10);
    iVar2 = *(int *)(lVar1 + 0x48) + 1;
    iVar4 = FUN_00aab488(lVar1,0xffffffff,0,0);
    iVar3 = 0;
    if (iVar4 != 0) {
      iVar3 = iVar2 / iVar4;
    }
    FUN_00aabe04(lVar1,uVar5,iVar2 - iVar3 * iVar4);
    return;
  }
  if (iVar2 == 3) {
    uVar5 = FUN_00457e1c();
    uVar6 = 0xb;
  }
  else {
    if (iVar2 != 0) {
      return;
    }
    uVar5 = FUN_00457e1c();
    uVar6 = 10;
  }
  FUN_00459efc(uVar5,uVar6,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadadc"></a> `00aadadc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aadae0"></a> `00aadae0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadae4"></a> `00aadae4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadae8"></a> `00aadae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aadaec"></a> `00aadaec` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aadaf0"></a> `00aadaf0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aadaf4"></a> `00aadaf4` | `c0 01 00 54` | b.eq 0x00aadb2c | `CONDITIONAL_JUMP`
<a id="insn-00aadaf8"></a> `00aadaf8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aadafc"></a> `00aadafc` | `a0 00 00 54` | b.eq 0x00aadb10 | `CONDITIONAL_JUMP`
<a id="insn-00aadb00"></a> `00aadb00` | `68 03 00 35` | cbnz w8,0x00aadb6c | `CONDITIONAL_JUMP`
<a id="insn-00aadb04"></a> `00aadb04` | `c6 a8 e6 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00aadb08"></a> `00aadb08` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aadb0c"></a> `00aadb0c` | `03 00 00 14` | b 0x00aadb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00aadb10"></a> `00aadb10` | `c3 a8 e6 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00aadb14"></a> `00aadb14` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aadb18"></a> `00aadb18` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aadb1c"></a> `00aadb1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadb20"></a> `00aadb20` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadb24"></a> `00aadb24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadb28"></a> `00aadb28` | `f5 b0 e6 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-00aadb2c"></a> `00aadb2c` | `13 d0 40 a9` | ldp x19,x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aadb30"></a> `00aadb30` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aadb34"></a> `00aadb34` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aadb38"></a> `00aadb38` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aadb3c"></a> `00aadb3c` | `68 4a 40 b9` | ldr w8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00aadb40"></a> `00aadb40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadb44"></a> `00aadb44` | `15 05 00 11` | add w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aadb48"></a> `00aadb48` | `50 f6 ff 97` | bl 0x00aab488 | `UNCONDITIONAL_CALL`
<a id="insn-00aadb4c"></a> `00aadb4c` | `a8 0e c0 1a` | sdiv w8,w21,w0 | `FALL_THROUGH`
<a id="insn-00aadb50"></a> `00aadb50` | `02 d5 00 1b` | msub w2,w8,w0,w21 | `FALL_THROUGH`
<a id="insn-00aadb54"></a> `00aadb54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadb58"></a> `00aadb58` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aadb5c"></a> `00aadb5c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadb60"></a> `00aadb60` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadb64"></a> `00aadb64` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadb68"></a> `00aadb68` | `a7 f8 ff 17` | b 0x00aabe04 | `CALL_TERMINATOR`
<a id="insn-00aadb6c"></a> `00aadb6c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aadb70"></a> `00aadb70` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadb74"></a> `00aadb74` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aadb78"></a> `00aadb78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadadc`](#insn-00aadadc) 範囲 `[['00aadadc', '00aadaf7']]`
  - `CONDITIONAL_JUMP` [`00aadaf4`](#insn-00aadaf4) → [`00aadb2c`](#insn-00aadb2c)
  - `FALL_THROUGH` [`00aadaf4`](#insn-00aadaf4) → [`00aadaf8`](#insn-00aadaf8)
- ブロック [`00aadaf8`](#insn-00aadaf8) 範囲 `[['00aadaf8', '00aadaff']]`
  - `CONDITIONAL_JUMP` [`00aadafc`](#insn-00aadafc) → [`00aadb10`](#insn-00aadb10)
  - `FALL_THROUGH` [`00aadafc`](#insn-00aadafc) → [`00aadb00`](#insn-00aadb00)
- ブロック [`00aadb00`](#insn-00aadb00) 範囲 `[['00aadb00', '00aadb03']]`
  - `CONDITIONAL_JUMP` [`00aadb00`](#insn-00aadb00) → [`00aadb6c`](#insn-00aadb6c)
  - `FALL_THROUGH` [`00aadb00`](#insn-00aadb00) → [`00aadb04`](#insn-00aadb04)
- ブロック [`00aadb04`](#insn-00aadb04) 範囲 `[['00aadb04', '00aadb0f']]`
  - `UNCONDITIONAL_JUMP` [`00aadb0c`](#insn-00aadb0c) → [`00aadb18`](#insn-00aadb18)
- ブロック [`00aadb10`](#insn-00aadb10) 範囲 `[['00aadb10', '00aadb17']]`
  - `FALL_THROUGH` [`00aadb14`](#insn-00aadb14) → [`00aadb18`](#insn-00aadb18)
- ブロック [`00aadb18`](#insn-00aadb18) 範囲 `[['00aadb18', '00aadb2b']]`
- ブロック [`00aadb2c`](#insn-00aadb2c) 範囲 `[['00aadb2c', '00aadb6b']]`
- ブロック [`00aadb6c`](#insn-00aadb6c) 範囲 `[['00aadb6c', '00aadb7b']]`

## 命令位置別の参照

- [`00aadadc`](#insn-00aadadc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadae0`](#insn-00aadae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadae4`](#insn-00aadae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadaf4`](#insn-00aadaf4) → [`00aadb2c`](#insn-00aadb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadafc`](#insn-00aadafc) → [`00aadb10`](#insn-00aadb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb00`](#insn-00aadb00) → [`00aadb6c`](#insn-00aadb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb04`](#insn-00aadb04) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00aadb0c`](#insn-00aadb0c) → [`00aadb18`](#insn-00aadb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb10`](#insn-00aadb10) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00aadb1c`](#insn-00aadb1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb20`](#insn-00aadb20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb24`](#insn-00aadb24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb28`](#insn-00aadb28) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00aadb48`](#insn-00aadb48) → [`00aab488`](../00aab/00aab488.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aab488` · 推定シンボル `None` · 推定型 `None`
- [`00aadb5c`](#insn-00aadb5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb60`](#insn-00aadb60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb64`](#insn-00aadb64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb68`](#insn-00aadb68) → [`00aabe04`](../00aab/00aabe04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aabe04` · 推定シンボル `None` · 推定型 `None`
- [`00aadb6c`](#insn-00aadb6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb70`](#insn-00aadb70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadb74`](#insn-00aadb74) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadadc`](#insn-00aadadc)

~~~json
{
  "source": "00aadadc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadae0`](#insn-00aadae0)

~~~json
{
  "source": "00aadae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadae4`](#insn-00aadae4)

~~~json
{
  "source": "00aadae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadaf4`](#insn-00aadaf4)

~~~json
{
  "source": "00aadaf4",
  "target": "00aadb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadafc`](#insn-00aadafc)

~~~json
{
  "source": "00aadafc",
  "target": "00aadb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb00`](#insn-00aadb00)

~~~json
{
  "source": "00aadb00",
  "target": "00aadb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb04`](#insn-00aadb04)

~~~json
{
  "source": "00aadb04",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb0c`](#insn-00aadb0c)

~~~json
{
  "source": "00aadb0c",
  "target": "00aadb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb10`](#insn-00aadb10)

~~~json
{
  "source": "00aadb10",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb1c`](#insn-00aadb1c)

~~~json
{
  "source": "00aadb1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb20`](#insn-00aadb20)

~~~json
{
  "source": "00aadb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb24`](#insn-00aadb24)

~~~json
{
  "source": "00aadb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb28`](#insn-00aadb28)

~~~json
{
  "source": "00aadb28",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb48`](#insn-00aadb48)

~~~json
{
  "source": "00aadb48",
  "target": "00aab488",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb5c`](#insn-00aadb5c)

~~~json
{
  "source": "00aadb5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb60`](#insn-00aadb60)

~~~json
{
  "source": "00aadb60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb64`](#insn-00aadb64)

~~~json
{
  "source": "00aadb64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb68`](#insn-00aadb68)

~~~json
{
  "source": "00aadb68",
  "target": "00aabe04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadb6c`](#insn-00aadb6c)

~~~json
{
  "source": "00aadb6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb70`](#insn-00aadb70)

~~~json
{
  "source": "00aadb70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadb74`](#insn-00aadb74)

~~~json
{
  "source": "00aadb74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
