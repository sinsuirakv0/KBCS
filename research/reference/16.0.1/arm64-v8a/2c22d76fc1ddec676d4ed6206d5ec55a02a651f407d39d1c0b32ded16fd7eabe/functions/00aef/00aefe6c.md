# 00aefe6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aefa44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-aebd96c6fe94c2388d2e693c8362ac70)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeff08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-4625e59e93e197a5398fbd14af2c2ef8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefe6c",
  "name": "FUN_00aefe6c",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ad8bc11dbd966ed12528034f026cef24d379de05c2ad4782dd03c9d435aa879",
  "source_text_sha256": "2ad8bc11dbd966ed12528034f026cef24d379de05c2ad4782dd03c9d435aa879",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefe6c",
        "00aeff53"
      ]
    ],
    "bytes_sha256": "95f340ae8684716ef95634e1e04c9b015ee591c0dc292f8caf03f530d21a5f47",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6ea4](../008b6/008b6ea4.md)
- [008b97a0](../008b9/008b97a0.md)
- [00a468f0](../00a46/00a468f0.md)
- [00a46bb8](../00a46/00a46bb8.md)
- [00aea354](../00aea/00aea354.md)
- [00aea5b0](../00aea/00aea5b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 966 bytes

~~~c

void FUN_00aefe6c(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*param_3 == 3) {
    uVar4 = *param_2;
    lVar5 = *(long *)(param_1 + 8);
    uVar2 = FUN_0047acf4();
    FUN_0047cdd4(uVar2,0xb,0);
    *(byte *)(lVar5 + 0x9ec) = *(byte *)(lVar5 + 0x9ec) ^ 1;
    uVar2 = FUN_008b6ea4(uVar4);
    uVar2 = FUN_00a468f0(uVar2,0);
    uVar3 = 0x90;
    if (*(char *)(lVar5 + 0x9ec) == '\0') {
      uVar3 = 0x91;
    }
    FUN_00a46bb8(uVar2,uVar3);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aea354(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008b97a0(uVar2,0,uVar1 & 1);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aea5b0(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008b97a0(uVar2,1,uVar1 & 1);
    return;
  }
  if (*param_3 == 0) {
    uVar2 = FUN_0047acf4();
    FUN_0047cdd4(uVar2,10,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefe6c"></a> `00aefe6c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aefe70"></a> `00aefe70` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefe74"></a> `00aefe74` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefe78"></a> `00aefe78` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefe7c"></a> `00aefe7c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aefe80"></a> `00aefe80` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aefe84"></a> `00aefe84` | `20 01 00 54` | b.eq 0x00aefea8 | `CONDITIONAL_JUMP`
<a id="insn-00aefe88"></a> `00aefe88` | `e8 05 00 35` | cbnz w8,0x00aeff44 | `CONDITIONAL_JUMP`
<a id="insn-00aefe8c"></a> `00aefe8c` | `9a 2b e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefe90"></a> `00aefe90` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aefe94"></a> `00aefe94` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefe98"></a> `00aefe98` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefe9c"></a> `00aefe9c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefea0"></a> `00aefea0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aefea4"></a> `00aefea4` | `cc 33 e6 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00aefea8"></a> `00aefea8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aefeac"></a> `00aefeac` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefeb0"></a> `00aefeb0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aefeb4"></a> `00aefeb4` | `90 2b e6 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefeb8"></a> `00aefeb8` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aefebc"></a> `00aefebc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefec0"></a> `00aefec0` | `c5 33 e6 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefec4"></a> `00aefec4` | `88 b2 67 39` | ldrb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00aefec8"></a> `00aefec8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefecc"></a> `00aefecc` | `08 01 00 52` | eor w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aefed0"></a> `00aefed0` | `88 b2 27 39` | strb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00aefed4"></a> `00aefed4` | `f4 1b f7 97` | bl 0x008b6ea4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefed8"></a> `00aefed8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefedc"></a> `00aefedc` | `85 5a fd 97` | bl 0x00a468f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aefee0"></a> `00aefee0` | `88 b2 67 39` | ldrb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00aefee4"></a> `00aefee4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aefee8"></a> `00aefee8` | `08 12 80 52` | mov w8,#0x90 | `FALL_THROUGH`
<a id="insn-00aefeec"></a> `00aefeec` | `01 15 88 1a` | cinc w1,w8,eq | `FALL_THROUGH`
<a id="insn-00aefef0"></a> `00aefef0` | `32 5b fd 97` | bl 0x00a46bb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefef4"></a> `00aefef4` | `81 b2 67 39` | ldrb w1,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00aefef8"></a> `00aefef8` | `b3 0a 40 f9` | ldr x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aefefc"></a> `00aefefc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeff00"></a> `00aeff00` | `15 e9 ff 97` | bl 0x00aea354 | `UNCONDITIONAL_CALL`
<a id="insn-00aeff04"></a> `00aeff04` | `02 00 00 12` | and w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aeff08"></a> `00aeff08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeff0c"></a> `00aeff0c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeff10"></a> `00aeff10` | `24 26 f7 97` | bl 0x008b97a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeff14"></a> `00aeff14` | `81 b2 67 39` | ldrb w1,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00aeff18"></a> `00aeff18` | `b3 0a 40 f9` | ldr x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aeff1c"></a> `00aeff1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeff20"></a> `00aeff20` | `a4 e9 ff 97` | bl 0x00aea5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeff24"></a> `00aeff24` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00aeff28"></a> `00aeff28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeff2c"></a> `00aeff2c` | `02 01 00 12` | and w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeff30"></a> `00aeff30` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aeff34"></a> `00aeff34` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeff38"></a> `00aeff38` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeff3c"></a> `00aeff3c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeff40"></a> `00aeff40` | `18 26 f7 17` | b 0x008b97a0 | `CALL_TERMINATOR`
<a id="insn-00aeff44"></a> `00aeff44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeff48"></a> `00aeff48` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeff4c"></a> `00aeff4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeff50"></a> `00aeff50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefe6c`](#insn-00aefe6c) 範囲 `[['00aefe6c', '00aefe87']]`
  - `CONDITIONAL_JUMP` [`00aefe84`](#insn-00aefe84) → [`00aefea8`](#insn-00aefea8)
  - `FALL_THROUGH` [`00aefe84`](#insn-00aefe84) → [`00aefe88`](#insn-00aefe88)
- ブロック [`00aefe88`](#insn-00aefe88) 範囲 `[['00aefe88', '00aefe8b']]`
  - `CONDITIONAL_JUMP` [`00aefe88`](#insn-00aefe88) → [`00aeff44`](#insn-00aeff44)
  - `FALL_THROUGH` [`00aefe88`](#insn-00aefe88) → [`00aefe8c`](#insn-00aefe8c)
- ブロック [`00aefe8c`](#insn-00aefe8c) 範囲 `[['00aefe8c', '00aefea7']]`
- ブロック [`00aefea8`](#insn-00aefea8) 範囲 `[['00aefea8', '00aeff43']]`
- ブロック [`00aeff44`](#insn-00aeff44) 範囲 `[['00aeff44', '00aeff53']]`

## 命令位置別の参照

- [`00aefe6c`](#insn-00aefe6c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe70`](#insn-00aefe70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe74`](#insn-00aefe74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe84`](#insn-00aefe84) → [`00aefea8`](#insn-00aefea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe88`](#insn-00aefe88) → [`00aeff44`](#insn-00aeff44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe8c`](#insn-00aefe8c) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aefe98`](#insn-00aefe98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe9c`](#insn-00aefe9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefea0`](#insn-00aefea0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefea4`](#insn-00aefea4) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aefeb4`](#insn-00aefeb4) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00aefec0`](#insn-00aefec0) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00aefed4`](#insn-00aefed4) → [`008b6ea4`](../008b6/008b6ea4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6ea4` · 推定シンボル `None` · 推定型 `None`
- [`00aefedc`](#insn-00aefedc) → [`00a468f0`](../00a46/00a468f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468f0` · 推定シンボル `None` · 推定型 `None`
- [`00aefef0`](#insn-00aefef0) → [`00a46bb8`](../00a46/00a46bb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46bb8` · 推定シンボル `None` · 推定型 `None`
- [`00aeff00`](#insn-00aeff00) → [`00aea354`](../00aea/00aea354.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aea354` · 推定シンボル `None` · 推定型 `None`
- [`00aeff10`](#insn-00aeff10) → [`008b97a0`](../008b9/008b97a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b97a0` · 推定シンボル `None` · 推定型 `None`
- [`00aeff20`](#insn-00aeff20) → [`00aea5b0`](../00aea/00aea5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aea5b0` · 推定シンボル `None` · 推定型 `None`
- [`00aeff34`](#insn-00aeff34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff38`](#insn-00aeff38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff3c`](#insn-00aeff3c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff40`](#insn-00aeff40) → [`008b97a0`](../008b9/008b97a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b97a0` · 推定シンボル `None` · 推定型 `None`
- [`00aeff44`](#insn-00aeff44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff48`](#insn-00aeff48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff4c`](#insn-00aeff4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefe6c`](#insn-00aefe6c)

~~~json
{
  "source": "00aefe6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe70`](#insn-00aefe70)

~~~json
{
  "source": "00aefe70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe74`](#insn-00aefe74)

~~~json
{
  "source": "00aefe74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe84`](#insn-00aefe84)

~~~json
{
  "source": "00aefe84",
  "target": "00aefea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe88`](#insn-00aefe88)

~~~json
{
  "source": "00aefe88",
  "target": "00aeff44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe8c`](#insn-00aefe8c)

~~~json
{
  "source": "00aefe8c",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefe98`](#insn-00aefe98)

~~~json
{
  "source": "00aefe98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe9c`](#insn-00aefe9c)

~~~json
{
  "source": "00aefe9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefea0`](#insn-00aefea0)

~~~json
{
  "source": "00aefea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefea4`](#insn-00aefea4)

~~~json
{
  "source": "00aefea4",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefeb4`](#insn-00aefeb4)

~~~json
{
  "source": "00aefeb4",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefec0`](#insn-00aefec0)

~~~json
{
  "source": "00aefec0",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefed4`](#insn-00aefed4)

~~~json
{
  "source": "00aefed4",
  "target": "008b6ea4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefedc`](#insn-00aefedc)

~~~json
{
  "source": "00aefedc",
  "target": "00a468f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefef0`](#insn-00aefef0)

~~~json
{
  "source": "00aefef0",
  "target": "00a46bb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff00`](#insn-00aeff00)

~~~json
{
  "source": "00aeff00",
  "target": "00aea354",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff10`](#insn-00aeff10)

~~~json
{
  "source": "00aeff10",
  "target": "008b97a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff20`](#insn-00aeff20)

~~~json
{
  "source": "00aeff20",
  "target": "00aea5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff34`](#insn-00aeff34)

~~~json
{
  "source": "00aeff34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff38`](#insn-00aeff38)

~~~json
{
  "source": "00aeff38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff3c`](#insn-00aeff3c)

~~~json
{
  "source": "00aeff3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff40`](#insn-00aeff40)

~~~json
{
  "source": "00aeff40",
  "target": "008b97a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff44`](#insn-00aeff44)

~~~json
{
  "source": "00aeff44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff48`](#insn-00aeff48)

~~~json
{
  "source": "00aeff48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff4c`](#insn-00aeff4c)

~~~json
{
  "source": "00aeff4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
