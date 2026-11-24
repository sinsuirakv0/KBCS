# 00bcfba8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcfb64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfb64.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-c4a0f21da03f19bbba991714cf0d467d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4c5f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-6b50ad4c28e4de6a87b423c3ab1d315a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfba8",
  "name": "FUN_00bcfba8",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21fd9b38544e74d243c4b5afb2a75bd05ee2d48b088895f4bc13a151ff39ea4c",
  "source_text_sha256": "21fd9b38544e74d243c4b5afb2a75bd05ee2d48b088895f4bc13a151ff39ea4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfba8",
        "00bcfc8b"
      ]
    ],
    "bytes_sha256": "e10e2f347451e044952b950e5dee886899479867bb3aca1236211409607e71c1",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc82d4](../00bc8/00bc82d4.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1780 bytes

~~~c

void FUN_00bcfba8(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  size_t sVar3;
  ulong uVar4;
  
                    /* try { // try from 00bcfbb4 to 00ccfbbb has its CatchHandler @ 00bcfd78 */
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
                    /* try { // try from 00bcfbdc to 00ccfbe3 has its CatchHandler @ 00bcfdf8 */
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
                    /* try { // try from 00bcfc10 to 00ccfc17 has its CatchHandler @ 00bcfde8 */
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5b;
                    /* try { // try from 00bcfc18 to 00ccfc77 has its CatchHandler @ 00bcfe10 */
  FUN_00bc82d4(param_1 + 0x10,param_2);
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5d;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfba8"></a> `00bcfba8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcfbac"></a> `00bcfbac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcfbb0"></a> `00bcfbb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfbb4"></a> `00bcfbb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcfbb8"></a> `00bcfbb8` | `28 a8 40 a9` | ldp x8,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfbbc"></a> `00bcfbbc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcfbc0"></a> `00bcfbc0` | `2b 20 40 b9` | ldr w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfbc4"></a> `00bcfbc4` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00bcfbc8"></a> `00bcfbc8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcfbcc"></a> `00bcfbcc` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfbd0"></a> `00bcfbd0` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfbd4"></a> `00bcfbd4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcfbd8"></a> `00bcfbd8` | `2b 20 00 b9` | str w11,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfbdc"></a> `00bcfbdc` | `69 01 00 54` | b.ls 0x00bcfc08 | `CONDITIONAL_JUMP`
<a id="insn-00bcfbe0"></a> `00bcfbe0` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfbe4"></a> `00bcfbe4` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcfbe8"></a> `00bcfbe8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfbec"></a> `00bcfbec` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfbf0"></a> `00bcfbf0` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfbf4"></a> `00bcfbf4` | `97 35 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfbf8"></a> `00bcfbf8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfbfc"></a> `00bcfbfc` | `40 04 00 b4` | cbz x0,0x00bcfc84 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc00"></a> `00bcfc00` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc04"></a> `00bcfc04` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc08"></a> `00bcfc08` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc0c"></a> `00bcfc0c` | `69 0b 80 52` | mov w9,#0x5b | `FALL_THROUGH`
<a id="insn-00bcfc10"></a> `00bcfc10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfc14"></a> `00bcfc14` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcfc18"></a> `00bcfc18` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfc1c"></a> `00bcfc1c` | `ae e1 ff 97` | bl 0x00bc82d4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc20"></a> `00bcfc20` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc24"></a> `00bcfc24` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfc28"></a> `00bcfc28` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfc2c"></a> `00bcfc2c` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc30"></a> `00bcfc30` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc34"></a> `00bcfc34` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfc38"></a> `00bcfc38` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcfc3c"></a> `00bcfc3c` | `69 01 00 54` | b.ls 0x00bcfc68 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc40"></a> `00bcfc40` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc44"></a> `00bcfc44` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcfc48"></a> `00bcfc48` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcfc4c"></a> `00bcfc4c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcfc50"></a> `00bcfc50` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfc54"></a> `00bcfc54` | `7f 35 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc58"></a> `00bcfc58` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcfc5c"></a> `00bcfc5c` | `60 01 00 b4` | cbz x0,0x00bcfc88 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc60"></a> `00bcfc60` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc64"></a> `00bcfc64` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc68"></a> `00bcfc68` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc6c"></a> `00bcfc6c` | `a9 0b 80 52` | mov w9,#0x5d | `FALL_THROUGH`
<a id="insn-00bcfc70"></a> `00bcfc70` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcfc74"></a> `00bcfc74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfc78"></a> `00bcfc78` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcfc7c"></a> `00bcfc7c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcfc80"></a> `00bcfc80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfc84"></a> `00bcfc84` | `8f 39 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bcfc88"></a> `00bcfc88` | `8e 39 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfba8`](#insn-00bcfba8) 範囲 `[['00bcfba8', '00bcfbb3']]`
  - `FALL_THROUGH` [`00bcfbb0`](#insn-00bcfbb0) → [`00bcfbb4`](#insn-00bcfbb4)
- ブロック [`00bcfbb4`](#insn-00bcfbb4) 範囲 `[['00bcfbb4', '00bcfbdb']]`
  - `FALL_THROUGH` [`00bcfbd8`](#insn-00bcfbd8) → [`00bcfbdc`](#insn-00bcfbdc)
- ブロック [`00bcfbdc`](#insn-00bcfbdc) 範囲 `[['00bcfbdc', '00bcfbdf']]`
  - `CONDITIONAL_JUMP` [`00bcfbdc`](#insn-00bcfbdc) → [`00bcfc08`](#insn-00bcfc08)
  - `FALL_THROUGH` [`00bcfbdc`](#insn-00bcfbdc) → [`00bcfbe0`](#insn-00bcfbe0)
- ブロック [`00bcfbe0`](#insn-00bcfbe0) 範囲 `[['00bcfbe0', '00bcfbff']]`
  - `CONDITIONAL_JUMP` [`00bcfbfc`](#insn-00bcfbfc) → [`00bcfc84`](#insn-00bcfc84)
  - `FALL_THROUGH` [`00bcfbfc`](#insn-00bcfbfc) → [`00bcfc00`](#insn-00bcfc00)
- ブロック [`00bcfc00`](#insn-00bcfc00) 範囲 `[['00bcfc00', '00bcfc07']]`
  - `FALL_THROUGH` [`00bcfc04`](#insn-00bcfc04) → [`00bcfc08`](#insn-00bcfc08)
- ブロック [`00bcfc08`](#insn-00bcfc08) 範囲 `[['00bcfc08', '00bcfc0f']]`
  - `FALL_THROUGH` [`00bcfc0c`](#insn-00bcfc0c) → [`00bcfc10`](#insn-00bcfc10)
- ブロック [`00bcfc10`](#insn-00bcfc10) 範囲 `[['00bcfc10', '00bcfc17']]`
  - `FALL_THROUGH` [`00bcfc14`](#insn-00bcfc14) → [`00bcfc18`](#insn-00bcfc18)
- ブロック [`00bcfc18`](#insn-00bcfc18) 範囲 `[['00bcfc18', '00bcfc3f']]`
  - `CONDITIONAL_JUMP` [`00bcfc3c`](#insn-00bcfc3c) → [`00bcfc68`](#insn-00bcfc68)
  - `FALL_THROUGH` [`00bcfc3c`](#insn-00bcfc3c) → [`00bcfc40`](#insn-00bcfc40)
- ブロック [`00bcfc40`](#insn-00bcfc40) 範囲 `[['00bcfc40', '00bcfc5f']]`
  - `CONDITIONAL_JUMP` [`00bcfc5c`](#insn-00bcfc5c) → [`00bcfc88`](#insn-00bcfc88)
  - `FALL_THROUGH` [`00bcfc5c`](#insn-00bcfc5c) → [`00bcfc60`](#insn-00bcfc60)
- ブロック [`00bcfc60`](#insn-00bcfc60) 範囲 `[['00bcfc60', '00bcfc67']]`
  - `FALL_THROUGH` [`00bcfc64`](#insn-00bcfc64) → [`00bcfc68`](#insn-00bcfc68)
- ブロック [`00bcfc68`](#insn-00bcfc68) 範囲 `[['00bcfc68', '00bcfc83']]`
- ブロック [`00bcfc84`](#insn-00bcfc84) 範囲 `[['00bcfc84', '00bcfc87']]`
- ブロック [`00bcfc88`](#insn-00bcfc88) 範囲 `[['00bcfc88', '00bcfc8b']]`

## 命令位置別の参照

- [`00bcfbac`](#insn-00bcfbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbb0`](#insn-00bcfbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbdc`](#insn-00bcfbdc) → [`00bcfc08`](#insn-00bcfc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbf4`](#insn-00bcfbf4) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbfc`](#insn-00bcfbfc) → [`00bcfc84`](#insn-00bcfc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc1c`](#insn-00bcfc1c) → [`00bc82d4`](../00bc8/00bc82d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc82d4` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc3c`](#insn-00bcfc3c) → [`00bcfc68`](#insn-00bcfc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc54`](#insn-00bcfc54) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc5c`](#insn-00bcfc5c) → [`00bcfc88`](#insn-00bcfc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc74`](#insn-00bcfc74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc78`](#insn-00bcfc78) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc84`](#insn-00bcfc84) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc88`](#insn-00bcfc88) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfbac`](#insn-00bcfbac)

~~~json
{
  "source": "00bcfbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbb0`](#insn-00bcfbb0)

~~~json
{
  "source": "00bcfbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbdc`](#insn-00bcfbdc)

~~~json
{
  "source": "00bcfbdc",
  "target": "00bcfc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbf4`](#insn-00bcfbf4)

~~~json
{
  "source": "00bcfbf4",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfbfc`](#insn-00bcfbfc)

~~~json
{
  "source": "00bcfbfc",
  "target": "00bcfc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc1c`](#insn-00bcfc1c)

~~~json
{
  "source": "00bcfc1c",
  "target": "00bc82d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc3c`](#insn-00bcfc3c)

~~~json
{
  "source": "00bcfc3c",
  "target": "00bcfc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc54`](#insn-00bcfc54)

~~~json
{
  "source": "00bcfc54",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc5c`](#insn-00bcfc5c)

~~~json
{
  "source": "00bcfc5c",
  "target": "00bcfc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc74`](#insn-00bcfc74)

~~~json
{
  "source": "00bcfc74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc78`](#insn-00bcfc78)

~~~json
{
  "source": "00bcfc78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc84`](#insn-00bcfc84)

~~~json
{
  "source": "00bcfc84",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc88`](#insn-00bcfc88)

~~~json
{
  "source": "00bcfc88",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
