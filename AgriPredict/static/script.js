// ========== CONFIGURATION ==========
// API runs on the same server - use relative URLs
const API_BASE_URL = ""

// ========== DOM ELEMENTS ==========
const elements = {
  form: document.getElementById("predictionForm"),
  stateSelect: document.getElementById("state"),
  districtSelect: document.getElementById("district"),
  marketSelect: document.getElementById("market"),
  commoditySelect: document.getElementById("commodity"),
  gradeSelect: document.getElementById("grade"),
  varietySelect: document.getElementById("variety"),
  dateInput: document.getElementById("date"),
  submitBtn: document.getElementById("submitBtn"),
  resultContainer: document.getElementById("resultContainer"),
  resultDetails: document.getElementById("resultDetails"),
  forecastContainer: document.getElementById("forecastContainer"),
  errorContainer: document.getElementById("errorContainer"),
  errorMessage: document.getElementById("errorMessage"),
  resetBtn: document.getElementById("resetBtn"),
  errorResetBtn: document.getElementById("errorResetBtn"),
  mobileMenuBtn: document.getElementById("mobileMenuBtn"),
}

// ========== INITIALIZATION ==========
document.addEventListener("DOMContentLoaded", () => {
  initializeApp()
})

function initializeApp() {
  setDefaultDate()
  loadStates()
  setupEventListeners()
}

// ========== DATE SETUP ==========
function setDefaultDate() {
  const tomorrow = new Date()
  tomorrow.setDate(tomorrow.getDate() + 1)
  const formattedDate = tomorrow.toISOString().split("T")[0]
  elements.dateInput.value = formattedDate
  elements.dateInput.min = formattedDate
}

// ========== EVENT LISTENERS ==========
function setupEventListeners() {
  // Cascading dropdown events
  elements.stateSelect.addEventListener("change", handleStateChange)
  elements.districtSelect.addEventListener("change", handleDistrictChange)
  elements.marketSelect.addEventListener("change", handleMarketChange)
  elements.commoditySelect.addEventListener("change", handleCommodityChange)
  elements.gradeSelect.addEventListener("change", handleGradeChange)

  // Form submission
  elements.form.addEventListener("submit", handleFormSubmit)

  // Reset buttons
  elements.resetBtn.addEventListener("click", resetForm)
  elements.errorResetBtn.addEventListener("click", resetForm)

  // Mobile menu
  if (elements.mobileMenuBtn) {
    elements.mobileMenuBtn.addEventListener("click", toggleMobileMenu)
  }

  // Smooth scroll for nav links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", smoothScroll)
  })
}

// ========== API FUNCTIONS ==========
async function fetchAPI(endpoint) {
  try {
    console.log(`Fetching: ${API_BASE_URL}${endpoint}`)
    const response = await fetch(`${API_BASE_URL}${endpoint}`)
    console.log(`Response status: ${response.status}`)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    console.log(`Data received:`, data)
    return data
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error)
    throw error
  }
}

async function postAPI(endpoint, data) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error)
    throw error
  }
}

// ========== DATA LOADING FUNCTIONS ==========
async function loadStates() {
  setSelectLoading(elements.stateSelect, "Loading states...")
  try {
    const states = await fetchAPI("/states")
    console.log("States loaded:", states)
    populateSelect(elements.stateSelect, states, "Select State")
    elements.stateSelect.disabled = false
  } catch (error) {
    console.error("Error loading states:", error)
    populateSelect(elements.stateSelect, [], "Error loading states - Check console")
    elements.stateSelect.disabled = false
  }
}

async function loadDistricts(state) {
  resetDependentSelects(["district", "market", "commodity", "grade", "variety"])
  setSelectLoading(elements.districtSelect, "Loading districts...")
  try {
    const districts = await fetchAPI(`/districts/${encodeURIComponent(state)}`)
    populateSelect(elements.districtSelect, districts, "Select District")
    elements.districtSelect.disabled = false
  } catch (error) {
    populateSelect(elements.districtSelect, [], "Error loading districts")
    elements.districtSelect.disabled = false
  }
}

async function loadMarkets(state, district) {
  resetDependentSelects(["market", "commodity", "grade", "variety"])
  setSelectLoading(elements.marketSelect, "Loading markets...")
  try {
    const markets = await fetchAPI(`/markets/${encodeURIComponent(state)}/${encodeURIComponent(district)}`)
    populateSelect(elements.marketSelect, markets, "Select Market")
    elements.marketSelect.disabled = false
  } catch (error) {
    populateSelect(elements.marketSelect, [], "Error loading markets")
    elements.marketSelect.disabled = false
  }
}

async function loadCommodities(state, district, market) {
  resetDependentSelects(["commodity", "grade", "variety"])
  setSelectLoading(elements.commoditySelect, "Loading commodities...")
  try {
    const commodities = await fetchAPI(
      `/commodities/${encodeURIComponent(state)}/${encodeURIComponent(district)}/${encodeURIComponent(market)}`,
    )
    populateSelect(elements.commoditySelect, commodities, "Select Commodity")
    elements.commoditySelect.disabled = false
  } catch (error) {
    populateSelect(elements.commoditySelect, [], "Error loading commodities")
    elements.commoditySelect.disabled = false
  }
}

async function loadGrades(state, district, market, commodity) {
  resetDependentSelects(["grade", "variety"])
  setSelectLoading(elements.gradeSelect, "Loading grades...")
  try {
    const grades = await fetchAPI(
      `/grades/${encodeURIComponent(state)}/${encodeURIComponent(district)}/${encodeURIComponent(market)}/${encodeURIComponent(commodity)}`,
    )
    populateSelect(elements.gradeSelect, grades, "Select Grade")
    elements.gradeSelect.disabled = false
  } catch (error) {
    populateSelect(elements.gradeSelect, [], "Error loading grades")
    elements.gradeSelect.disabled = false
  }
}

async function loadVarieties(state, district, market, commodity, grade) {
  resetDependentSelects(["variety"])
  setSelectLoading(elements.varietySelect, "Loading varieties...")
  try {
    const varieties = await fetchAPI(
      `/varieties/${encodeURIComponent(state)}/${encodeURIComponent(district)}/${encodeURIComponent(market)}/${encodeURIComponent(commodity)}/${encodeURIComponent(grade)}`,
    )
    populateSelect(elements.varietySelect, varieties, "Select Variety")
    elements.varietySelect.disabled = false
  } catch (error) {
    populateSelect(elements.varietySelect, [], "Error loading varieties")
    elements.varietySelect.disabled = false
  }
}

// ========== SELECT HELPER FUNCTIONS ==========
function setSelectLoading(selectElement, message) {
  selectElement.innerHTML = `<option value="">${message}</option>`
  selectElement.classList.add("loading")
  selectElement.disabled = true
}

function populateSelect(selectElement, options, placeholder) {
  selectElement.classList.remove("loading")
  selectElement.innerHTML = `<option value="">${placeholder}</option>`

  options.forEach((option) => {
    const opt = document.createElement("option")
    opt.value = option
    opt.textContent = option
    selectElement.appendChild(opt)
  })
}

function resetDependentSelects(selectIds) {
  const placeholders = {
    district: "Select state first",
    market: "Select district first",
    commodity: "Select market first",
    grade: "Select commodity first",
    variety: "Select grade first",
  }

  selectIds.forEach((id) => {
    const select = elements[`${id}Select`]
    select.innerHTML = `<option value="">${placeholders[id]}</option>`
    select.disabled = true
    select.classList.remove("loading")
  })
}

// ========== EVENT HANDLERS ==========
function handleStateChange(e) {
  const state = e.target.value
  if (state) {
    loadDistricts(state)
  } else {
    resetDependentSelects(["district", "market", "commodity", "grade", "variety"])
  }
}

function handleDistrictChange(e) {
  const state = elements.stateSelect.value
  const district = e.target.value
  if (district) {
    loadMarkets(state, district)
  } else {
    resetDependentSelects(["market", "commodity", "grade", "variety"])
  }
}

function handleMarketChange(e) {
  const state = elements.stateSelect.value
  const district = elements.districtSelect.value
  const market = e.target.value
  if (market) {
    loadCommodities(state, district, market)
  } else {
    resetDependentSelects(["commodity", "grade", "variety"])
  }
}

function handleCommodityChange(e) {
  const state = elements.stateSelect.value
  const district = elements.districtSelect.value
  const market = elements.marketSelect.value
  const commodity = e.target.value
  if (commodity) {
    loadGrades(state, district, market, commodity)
  } else {
    resetDependentSelects(["grade", "variety"])
  }
}

function handleGradeChange(e) {
  const state = elements.stateSelect.value
  const district = elements.districtSelect.value
  const market = elements.marketSelect.value
  const commodity = elements.commoditySelect.value
  const grade = e.target.value
  if (grade) {
    loadVarieties(state, district, market, commodity, grade)
  } else {
    resetDependentSelects(["variety"])
  }
}

// ========== FORM SUBMISSION ==========
async function handleFormSubmit(e) {
  e.preventDefault()

  // Validate form
  if (!validateForm()) {
    return
  }

  // Get form data
  const formData = {
    state: elements.stateSelect.value,
    district: elements.districtSelect.value,
    market: elements.marketSelect.value,
    commodity: elements.commoditySelect.value,
    grade: elements.gradeSelect.value,
    variety: elements.varietySelect.value,
    date: elements.dateInput.value,
  }

  // Show loading state
  setLoadingState(true)
  hideResults()

  try {
    // Call prediction API
    const response = await postAPI("/predict", formData)

    if (response.status === "success") {
      displayResults(formData, response.forecast)
    } else {
      displayError(response.message || "Prediction failed. Please try again.")
    }
  } catch (error) {
    displayError("Failed to connect to the server. Please check if the backend is running.")
  } finally {
    setLoadingState(false)
  }
}

// ========== VALIDATION ==========
function validateForm() {
  let isValid = true
  const fields = ["state", "district", "market", "commodity", "grade", "variety", "date"]

  fields.forEach((field) => {
    const element = field === "date" ? elements.dateInput : elements[`${field}Select`]
    const errorElement = document.getElementById(`${field}Error`)

    if (!element.value) {
      errorElement.textContent = `Please select a ${field}`
      isValid = false
    } else {
      errorElement.textContent = ""
    }
  })

  return isValid
}

// ========== UI STATE FUNCTIONS ==========
function setLoadingState(isLoading) {
  elements.submitBtn.classList.toggle("loading", isLoading)
  elements.submitBtn.disabled = isLoading
}

function hideResults() {
  elements.resultContainer.classList.remove("show")
  elements.errorContainer.classList.remove("show")
}

// ========== RESULT DISPLAY ==========
function displayResults(formData, forecast) {
  // Generate result details HTML
  elements.resultDetails.innerHTML = `
        <div class="result-detail-item">
            <span class="result-detail-label">State</span>
            <span class="result-detail-value">${formData.state}</span>
        </div>
        <div class="result-detail-item">
            <span class="result-detail-label">District</span>
            <span class="result-detail-value">${formData.district}</span>
        </div>
        <div class="result-detail-item">
            <span class="result-detail-label">Market</span>
            <span class="result-detail-value">${formData.market}</span>
        </div>
        <div class="result-detail-item">
            <span class="result-detail-label">Commodity</span>
            <span class="result-detail-value">${formData.commodity}</span>
        </div>
        <div class="result-detail-item">
            <span class="result-detail-label">Grade</span>
            <span class="result-detail-value">${formData.grade}</span>
        </div>
        <div class="result-detail-item">
            <span class="result-detail-label">Variety</span>
            <span class="result-detail-value">${formData.variety}</span>
        </div>
    `

  // Generate forecast grid
  const startDate = new Date(formData.date)
  const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

  let forecastHTML = '<div class="forecast-grid">'
  forecast.forEach((price, index) => {
    const forecastDate = new Date(startDate)
    forecastDate.setDate(startDate.getDate() + index)

    const dayName = dayNames[forecastDate.getDay()]
    const dateStr = forecastDate.toLocaleDateString("en-IN", { day: "numeric", month: "short" })
    const isToday = index === 0

    forecastHTML += `
            <div class="forecast-day ${isToday ? "today" : ""}">
                <span class="forecast-date">${dateStr}</span>
                <span class="forecast-day-name">${isToday ? "Day 1" : `Day ${index + 1}`}</span>
                <span class="forecast-price">₹${price.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
            </div>
        `
  })
  forecastHTML += "</div>"

  elements.forecastContainer.innerHTML = forecastHTML

  // Show results
  elements.resultContainer.classList.add("show")
  elements.errorContainer.classList.remove("show")

  // Scroll to results
  elements.resultContainer.scrollIntoView({ behavior: "smooth", block: "center" })
}

function displayError(message) {
  elements.errorMessage.textContent = message
  elements.errorContainer.classList.add("show")
  elements.resultContainer.classList.remove("show")

  elements.errorContainer.scrollIntoView({ behavior: "smooth", block: "center" })
}

// ========== RESET FORM ==========
function resetForm() {
  elements.form.reset()
  setDefaultDate()
  resetDependentSelects(["district", "market", "commodity", "grade", "variety"])
  hideResults()

  // Clear error messages
  document.querySelectorAll(".error-message").forEach((el) => {
    el.textContent = ""
  })

  // Scroll to form
  document.getElementById("predict").scrollIntoView({ behavior: "smooth" })
}

// ========== NAVIGATION ==========
function toggleMobileMenu() {
  const navLinks = document.querySelector(".nav-links")
  navLinks.classList.toggle("active")
}

function smoothScroll(e) {
  e.preventDefault()
  const targetId = e.currentTarget.getAttribute("href")
  const targetElement = document.querySelector(targetId)

  if (targetElement) {
    targetElement.scrollIntoView({ behavior: "smooth" })
  }
}