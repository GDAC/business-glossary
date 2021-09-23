// @ts-check
// Module gdac/abstract
// Handle the abstract section properly.
import { getIntlData, showError } from "../core/utils.js";
export const name = "gdac/abstract";

const localizationStrings = {
  en: {
    abstract: "Abstract",
  },
  ko: {
    abstract: "요약",
  },
  zh: {
    abstract: "摘要",
  },
  ja: {
    abstract: "要約",
  },
  nl: {
    abstract: "Samenvatting",
  },
  es: {
    abstract: "Resumen",
  },
  de: {
    abstract: "Zusammenfassung",
  },
};
const l10n = getIntlData(localizationStrings);

export async function run() {
  const abs = document.getElementById("abstract");
  abs.classList.add("introductory");
  let abstractHeading = document.querySelector("#abstract>h2");
  if (abstractHeading) {
    return;
  }
  abstractHeading = document.createElement("h2");
  abstractHeading.textContent = l10n.abstract;
  abs.prepend(abstractHeading);
}
